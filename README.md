# Currently Under Maintenance

# KoalaBeatzHunter

Cross-platform mobile MP3 downloader and converter.

## Available GUI's
<table>
  <tr>
    <th>UI</th><th>View</th><th>Implemented</th>
  </tr>
  <tr>
    <td>Tkinter</td><td>✓</td><td>x</td>
  </tr>
  <tr>
    <td>Kivy</td><td>✓</td><td>✓</td>
  </tr>
</table>

## Limitations

* It works only with the Youtube website using the *pytube* package.
* It works with the MP4 format, which is pretty much every video's.
* It chooses only the best format of the video to download.
* It does not support over crowded youtube videos of Miley Cyrus with 999,999,999 views.

## Dependencies

<table>
  <tr>
    <th>Purpose</th><th>Technology</th><th>Weight</th><th>Cross-platform</th>
  </tr>
  <tr>
    <td>Download Youtube Video</td><td>pytube</td><td>4kB</td><td>Yes</td>
  </tr>
  <tr>
    <td>Convert Mp4 to Mp3</td><td>FFmpeg</td><td>248kB</td><td>Yes</td>
  </tr>
  <tr>
    <td>Write Mp3 Metadata</td><td>Mutagen</td><td>813kB</td><td>Yes</td>
  </tr>
</table>

## Instructions

### Debian

    sudo apt-get install python-kivy python-tk
    pip install -r requirements.txt --user

## Terms

<table>
  <tr>
    <th>Term</th><th>Definition</th>
  </tr>
  <tr>
    <td>App</td><td>Controller</td>
  </tr>
  <tr>
    <td>View</td><td>User Interface</td>
  </tr>
</table>

# Encountered Issues

* Can't update a field from an outside thread started elsewhere than in the KivyView from the user action.

	I have to break my MVC Pattern: View <-- Controller --> Model. During the update of the ProgressBar value from the outside thread, I get the new progression value but nothing changes on the screen. Therefore, I'm not able to call my controller to start the downloading thread and I have to start the thread from the KivyView directly.

	* Solution

	    View <--> Controller <--> Model
		
* Kivy has default help options that I did not manage to overwrite.

    * Solution

        I binded different arguments to the KoalaBeatzHunter help options.
        
        * Kivy Default
        
                ./KoalaBeatzHunter.py -h
            
        * KoalaBeatzHunter
        
                ./KoalaBeatzHunter.py h?

