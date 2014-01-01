KoalaBeatzHunter
================
Cross-platform MVC url to mp3 converter

<b>Terms</b>
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

<b>Available UI</b>
<table>
  <tr>
    <th>UI</th><th>Got View</th><th>Status</th>
  </tr>
  <tr>
    <td>Tkinter</td><td>Yes</td><td>Under Construction</td>
  </tr>
  <tr>
    <td>Kivy</td><td>Yes</td><td>Under Construction</td>
  </tr>
</table>

Problems
--------
1. Kivy: Cant update a field from an outside thread started by someone else than the KivyView from the user action.
	* <b>Consequences</b>

		> I have to break my MVC Pattern. View <-- Controller --> Data, Tools etc.

	* <b>Explanations</b>

		> When i update the ProgressBar.value from outside thread, i can print and see the new value
		> but nothing changes on screen so far... So i cant call my controller to start the downloading
		> thread that will update my ProgressBar. Unstead i have to start the thread from the kiwi application directly.

	* <b>Solution</b>

		> View <--> Controller <--> Data, Tools etc.

Notes
-----
      I will think before using Tkinter.
      I will try to avoid using Tkinter.
      I will never use Tkinter.
Kivy is awesome.
