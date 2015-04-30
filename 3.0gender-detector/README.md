Gender Detector
===============
Do the process below:

Gender detector is a Python library for guessing a person's gender by his/her first name. This library is based on [beauvoir](https://github.com/jeremybmerrill/beauvoir) with support for United States, United Kingdom,  Argentina and Uruguay.

**This is still in beta stages, use with precaution**

© 2014 Marcos Vanetta. Available under GPL2 License. See LICENSE.

Datasets
========

* UK, from `OpenGenderTracking project <http://opengendertracking.github.com>`_
* US, from `OpenGenderTracking project <http://opengendertracking.github.com>`_
* AR, from `Names query site <http://www.buenosaires.gob.ar/areas/registrocivil/nombres/busqueda/buscador_nombres.php?menu_id=16082>`_ from the goverment of the City of Buenos Aires. **this is a small sample, use with precaution!**.
* UY, from `Civil registry <https://catalogodatos.gub.uy/dataset/partidas-de-registro-civil-de-montevideo>`_) in Montevideo. Same as in AR, **Use with precaution!**

How to use it
=============

Nothing too fancy, just install:

.. code-block:: bash

    pip install gender-detector

And then:

.. code-block:: python

    from gender_detector import GenderDetector
    detector = GenderDetector('us') # It can also be ar, uk, uy.
    detector.guess('Marcos') # => 'male'

##Note

After you are done installing <a href= "https://github.com/grantjenks/wordsegment"> Word segment</a> and <a href="https://github.com/malev/gender-detector"> gender detector</a> <br>
you do the following:
1.Copy the test_gender.py and.TSV file in the gender detector folder as I have done.<br>
2.once you run the test_gender.py file, it will extract the usernames from .TSV file,<br>
3.remove the unrequired additions to the username( eg hero_111 to hero) and use the word segment module<br>
4.to break it into words(like TheIncerdibleHulk=> 'the', 'Incredible', 'hulk') and then use these words to predict gender.<br>
5.all the required files are supplied. Before and after of usernames are printed in names.txt and names_processed.txt.

