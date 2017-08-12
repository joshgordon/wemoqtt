wemoqtt
=======

This is a quick saturday-morning hack to turn mqtt messages into controlling a wemo.

Using it!
---------
docker build -t wemoqtt .
docker run -d --net=host wemoqtt

If you want to change what topic is being listened on, it's right in script.py. (See previous comment about quick saturday-morning hackjob on this)
