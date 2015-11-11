#  VR Assistant

Instructions for setup
------------

- Clone the project

        git clone git@github.com:iamgroot42/PseudoJarvis.git VR_Assistant
        cd VR_Assistant
        
- Install following python packages:

        pip install pytube
        pip install json
        pip install requests
        pip install tungsten
        pip install facepy
        pip install subprocess
        pip install tts_manage
        pip install flask

Using the Script
------------

        1. Get a Facebook access token and paste it into the server.py file 
        2. Get a Youtube developer access token and paste it into the server.py file 
        5. Run 'nodejs html2img.js' 
        6. Run 'python server.py'

Note
------------

*  Any command preceded by 'jarvis play ' will open the first YouTube video corresponding to the search term and play it.
*  Any command containing the keyword 'facebook' will switch back to Facebook posts
*  Any other command will use Wolfram Alpha's API to answer the given query.
*  Opening the home page displays a random number (to make sure the server is running, used for debugging).
