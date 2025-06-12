# from pydub import AudioSegment
# import os

# # Replace these with your actual paths
# input_dir = "<archive>/VoxCeleb1/wav"  # Path to your original dataset
# output_dir = "<your_path>/IndianVoxCeleb1/wav"  # Path where converted files will go

# # Create output directory if it doesn’t exist
# os.makedirs(output_dir, exist_ok=True)

# # Loop through speakers, YouTube IDs, and WAV files
# for speaker in os.listdir(input_dir):
#     speaker_dir = os.path.join(input_dir, speaker)
#     if not os.path.isdir(speaker_dir):
#         continue
#     for yt_id in os.listdir(speaker_dir):
#         yt_dir = os.path.join(speaker_dir, yt_id)
#         if not os.path.isdir(yt_dir):
#             continue
#         for wav in os.listdir(yt_dir):
#             if wav.endswith(".wav"):
#                 # Load the WAV file
#                 wav_path = os.path.join(yt_dir, wav)
#                 audio = AudioSegment.from_wav(wav_path)
                
#                 # Convert to 22050 Hz, mono (1 channel)
#                 audio = audio.set_frame_rate(22050).set_channels(1)
                
#                 # Create output path
#                 out_path = os.path.join(output_dir, speaker, yt_id)
#                 os.makedirs(out_path, exist_ok=True)
                
#                 # Save the converted file
#                 audio.export(os.path.join(out_path, wav), format="wav")
#                 print(f"Converted: {wav_path} -> {out_path}/{wav}")