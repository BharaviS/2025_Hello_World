import pyttsx3
import threading
import time
import re
from queue import Queue, Empty

class TTSController:
    def __init__(self):
        self.engine = None
        self.is_speaking = False
        self.is_paused = False
        self.should_stop = False
        self.current_text = ""
        self.words = []
        self.current_word_index = 0
        self.words_per_minute = 200
        self.skip_words_count = 15  # Approximate words in 5 seconds
        
        # Thread control
        self.speak_thread = None
        self.lock = threading.Lock()
        
        # Initialize engine
        self._initialize_engine()
    
    def _initialize_engine(self):
        """Initialize the TTS engine"""
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', self.words_per_minute)
            
            # Set up engine callbacks
            self.engine.connect('started-utterance', self._on_start)
            self.engine.connect('finished-utterance', self._on_end)
            
        except Exception as e:
            print(f"Error initializing TTS engine: {e}")
            raise
    
    def _on_start(self, name):
        """Callback when utterance starts"""
        self.is_speaking = True
    
    def _on_end(self, name, completed):
        """Callback when utterance ends"""
        self.is_speaking = False
    
    def get_voices(self):
        """Get available voices"""
        try:
            voices = self.engine.getProperty('voices')
            voice_list = []
            for i, voice in enumerate(voices):
                voice_list.append({
                    'id': voice.id,
                    'name': voice.name if hasattr(voice, 'name') else f"Voice {i+1}",
                    'languages': voice.languages if hasattr(voice, 'languages') else []
                })
            return voice_list
        except Exception as e:
            print(f"Error getting voices: {e}")
            return [{'id': 'default', 'name': 'Default Voice'}]
    
    def set_voice(self, voice_id):
        """Set the voice to use"""
        try:
            self.engine.setProperty('voice', voice_id)
        except Exception as e:
            print(f"Error setting voice: {e}")
    
    def set_rate(self, rate):
        """Set speech rate (words per minute)"""
        try:
            self.words_per_minute = rate
            self.engine.setProperty('rate', rate)
            # Update skip calculation based on new rate
            self.skip_words_count = max(1, (rate * 5) // 60)  # 5 seconds worth of words
        except Exception as e:
            print(f"Error setting rate: {e}")
    
    def _prepare_text(self, text):
        """Prepare text for word-by-word processing"""
        # Split text into words, preserving punctuation context
        words = re.findall(r'\S+', text)
        return words
    
    def speak_text(self, text, progress_callback=None, finished_callback=None):
        """Speak text with progress tracking"""
        with self.lock:
            self.should_stop = False
            self.is_paused = False
            self.current_text = text
            self.words = self._prepare_text(text)
            self.current_word_index = 0
        
        if not self.words:
            if finished_callback:
                finished_callback()
            return
        
        # Start speaking in chunks to allow for interruption
        self._speak_with_progress(progress_callback, finished_callback)
    
    def _speak_with_progress(self, progress_callback, finished_callback):
        """Speak text with progress updates and interruption support"""
        chunk_size = 10  # Words per chunk
        
        while self.current_word_index < len(self.words) and not self.should_stop:
            if self.is_paused:
                time.sleep(0.1)
                continue
            
            # Get next chunk of words
            end_index = min(self.current_word_index + chunk_size, len(self.words))
            chunk_words = self.words[self.current_word_index:end_index]
            chunk_text = ' '.join(chunk_words)
            
            # Speak the chunk
            try:
                self.engine.say(chunk_text)
                self.engine.runAndWait()
                
                # Update progress
                if not self.should_stop:
                    self.current_word_index = end_index
                    if progress_callback:
                        progress_callback(self.current_word_index, len(self.words))
                
                # Small delay to allow for interruption
                time.sleep(0.1)
                
            except Exception as e:
                print(f"Error during speech: {e}")
                break
        
        # Call finished callback if we completed successfully
        if finished_callback and not self.should_stop:
            finished_callback()
    
    def pause(self):
        """Pause speech"""
        with self.lock:
            self.is_paused = True
        
        # Stop current utterance
        try:
            self.engine.stop()
        except:
            pass
    
    def resume(self):
        """Resume speech"""
        with self.lock:
            self.is_paused = False
    
    def stop(self):
        """Stop speech completely"""
        with self.lock:
            self.should_stop = True
            self.is_paused = False
            self.current_word_index = 0
        
        try:
            self.engine.stop()
        except:
            pass
    
    def skip_forward(self):
        """Skip forward approximately 5 seconds"""
        with self.lock:
            if self.words and self.current_word_index < len(self.words):
                # Calculate new position
                new_index = min(
                    self.current_word_index + self.skip_words_count,
                    len(self.words)
                )
                
                # Stop current speech
                try:
                    self.engine.stop()
                except:
                    pass
                
                # Update position
                self.current_word_index = new_index
                
                # If we're at the end, stop completely
                if self.current_word_index >= len(self.words):
                    self.should_stop = True
    
    def skip_backward(self):
        """Skip backward approximately 5 seconds"""
        with self.lock:
            if self.words and self.current_word_index > 0:
                # Calculate new position
                new_index = max(
                    self.current_word_index - self.skip_words_count,
                    0
                )
                
                # Stop current speech
                try:
                    self.engine.stop()
                except:
                    pass
                
                # Update position
                self.current_word_index = new_index
    
    def cleanup(self):
        """Clean up resources"""
        self.stop()
        
        if self.engine:
            try:
                self.engine.stop()
            except:
                pass
