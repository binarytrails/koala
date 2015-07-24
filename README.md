# Currently Under Maintenance

# Koala

Cross-platform mobile MP3 downloader and converter. The default UI is written in Kivy.

## Limitations

* It works only with the Youtube website using the *TODO* package.
* It works with the MP4 format, which is pretty much every video's.
* It chooses only the best format of the video to download.
* It does not support over crowded youtube videos of Miley Cyrus with 999,999,999 views.

## Dependencies

* TODO      Downloader(s)
* FFmpeg    MP4 -> MP3
* Mutagen   Write MP3 Metadata

## Instructions

### Debian

    sudo apt-get install python-kivy python-tk
    pip install -r requirements.txt --user

# Encountered Issues

* Can't update a field from an outside thread started elsewhere than in the KivyView from the user action.

	I have to break my MVC Pattern: View <-- Controller --> Model. During the update of the ProgressBar value from the outside thread, I get the new progression value but nothing changes on the screen. Therefore, I'm not able to call my controller to start the downloading thread and I have to start the thread from the KivyView directly.

	* Solution

	    View <--> Controller <--> Model
		
* Kivy has default help options that I did not manage to overwrite.

    * Solution

        I binded different arguments to the Koala help options.
        
        * Kivy Default
        
                ./Koala.py -h
            
        * Koala's way
        
                ./Koala.py h?

