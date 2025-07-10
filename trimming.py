from pydub import AudioSegment
import os
import datetime 

output_folder = "Audio/audio5_trimmed"
os.makedirs(output_folder, exist_ok = True)
input_path = "Audio/audio5/HOA HẬU làm được nhiều hơn ngoài 'XINH ĐẸP'.wav" # CHANGE THIS
filename = os.path.splitext(os.path.basename(input_path))[0]  
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Load the full .wav file
audio = AudioSegment.from_wav(input_path)

def start_time(minute: int, second: int) -> int:
    """
    Convert start time from minutes and seconds to milliseconds.

    Args:
        minute (int): The starting minute.
        second (int): The starting second.

    Returns:
        int: Start time in milliseconds.
    """
    return ((minute * 60) + second) * 1000

def end_time(hour: int, minute: int, second: int) -> int:
    """
    Convert end time from hours, minutes, and seconds to milliseconds.

    Args:
        hour (int): The ending hour.
        minute (int): The ending minute.
        second (int): The ending second.

    Returns:
        int: End time in milliseconds.
    """
    return ((hour * 60 * 60) + (minute * 60) + second) * 1000


# Trimming
trimmed_five = audio[start_time(1, 11):end_time(0, 33, 18)] # CHANGE THIS

output_path = os.path.join(output_folder, f"{filename}_trimmed_{timestamp}.wav")
# Export to a new file
trimmed_five.export(output_path, format="wav", parameters=["-ar", "16000"])
