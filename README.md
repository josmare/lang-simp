# Lang Simplification App

This app has been deployed to:

[AWS Elastic Beanstalk Link](http://langsimp-env.eba-nmaxzbn9.eu-north-1.elasticbeanstalk.com/)

By default, it plots the math function in python-numpy format:
```
np.exp(-t) * np.cos(2*np.pi*t)
```

which is equivalent to:


<img src="https://render.githubusercontent.com/render/math?math=f(t)= e^{-t} cos(2 \pi*t)">

using 500 units in _x_ axis (this value is fixed). I choose this function just because it looks pretty and shows in a nice way how the algorithm works.


Also uses default values of:

```
tolerance = 2
look_ahead= 40
```
Then you can play with these values, and a new valid formula in the fields given for this purpose.
An easy formula example can be:

```
np.cos(2*np.pi*t)
```

The app wasn't packaged in any form because is intended to be tried on the online version.

If you wish to install it in local environment:

* Create python virtual environment
* Install requirements.txt
* Set ``FLASK_APP='application.py`` to your environment variables
* Run ``flask run``

