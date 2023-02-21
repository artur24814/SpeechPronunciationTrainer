# SpeechPronunciationTrainer


<img src='https://kivymd.readthedocs.io/en/1.0.1/_static/logo-kivymd.png' weight='300' height='300'>
<hr>

## Contents
 * <a href="#info"><strong>Info</strong></a><p>Information about the resources used in this project</p>
 * <a href="#SpeechPronunciationTrainer"><strong>Gim Manager</strong></a><p>Mobile app to listen text in english and train your pronunciation. </p>
 * <a href="#clone_project"><strong>Clone and Run Project</strong></a><p>how run projects in your computer or in telephone</p>

<hr>

<details><summary id="info" style="font-size: 30px;"> INFO</summary>
<h4>Information about the additional library, external Api used in this project and general information</h4>

<strong>Kivy</strong> A software library for rapid development of hardware-accelerated multitouch applications..

<strong>Pillow</strong> The Python Imaging Library adds image processing capabilities to your Python interpreter.

<strong>Buldozer</strong> Buildozer is a tool that aim to package mobiles application easily. It automates the entire build process, download the prerequisites like python-for-android, Android SDK, NDK, etc.

<strong>SpeechRecognition </strong> Library for performing speech recognition, with support for several engines and APIs, online and offline..

</details>

<hr>
<center><h1 id="SpeechPronunciationTrainer"> Speech Pronunciation Trainer <span style='font-size:80px;'><img src="https://img.icons8.com/external-microdots-premium-microdot-graphic/64/null/external-holiday-christmas-new-year-vol2-microdots-premium-microdot-graphic-3.png"/></span></h1></center>
First Page 'Speach Trainer'


Type or copy text and start training. You can listen to the pronunciation of this text. Or click on the microphone and try to repeat this text.

<center><img src='https://user-images.githubusercontent.com/97242088/220396308-a3733a25-069b-4afe-9f5e-e0ecc913efb8.png' alt='first-image'></center>

When you stop speaking, you will see the speech recognition result on the screen.

<center><img src='https://user-images.githubusercontent.com/97242088/220415137-ea21df0d-b991-45f8-bc20-73000c8ddf03.png' alt='second-image'></center>

Click the 'check' button and you'll see which word you made a mistake in.

<center><img src='https://user-images.githubusercontent.com/97242088/220415155-ba9093ba-6dfd-4421-8352-8a82efacfc1b.png' alt='5-image'></center>

<center><img src='https://user-images.githubusercontent.com/97242088/220415072-a5a5c0d5-a113-4ea0-8187-4e9785611805.png' alt='3-image'>
<img src='https://user-images.githubusercontent.com/97242088/220415086-0fc5d157-95cf-4787-ac74-b9a81e776e62.png' alt='4-image'></center>

<hr>

<center><h2 id="clone_project">Clone and Run a Project</h2></center>

Before diving let’s look at the things we are required to install in our system.

To run App prefer to use the Virtual Environment

`pip install --upgrade pip setuptools wheel`
`pip install virtualenv`

Making and Activating the Virtual Environment:-

`python -m venv “name as you like”`

`source env/bin/activate`

Installing Kivy:-

`pip install -r requirements.txt`


Now, we need to clone my project from Github:-
<p>Above the list of files, click Code.</p>
<img src="https://docs.github.com/assets/cb-20363/images/help/repository/code-button.png">

Copy the URL for the repository.
<ul>
<li>To clone the repository using HTTPS, under "HTTPS", click</li>
<li>To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click</li>
<li>To clone a repository using GitHub CLI, click GitHub CLI, then click</li>
</ul>
<img src="https://docs.github.com/assets/cb-33207/images/help/repository/https-url-clone-cli.png">

Open Terminal.

Change the current working directory to the location where you want the cloned directory.

Type git clone, and then paste the URL you copied earlier.

`$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`

Press Enter to create your local clone.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...<br>
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Install the project dependencies:

`pip install -r requirements.txt`

to run

`python main.py --size 250x500`


Have fun
<p style="font-size:100px">&#129409;</p>

