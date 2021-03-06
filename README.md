# Portfolio analysis

This api can provide you with 5 coefficints to analyze your stock portfolio.
- Coefficient of variation
- Sharpe ratio
- Information coefficient
- Sortino coefficient
- Treynor ratio

## Gui

### Installation
Simply download archive and unzip to desired folder

```shell
cd ~/path_to_folder
python3 Main.py
```

![alt text](https://github.com/Jabca/EconomicApi/blob/master/gui/resources/gui_exp.png?raw=true)
-To add company type it's token, number
-Press Add button or type Enter

## To see api in action



Choose conmpany any pass it's ticker as argument
If you want to specify the amount of years take to account you can add this as keyword argument depth 

```py
from portfoloio_analysis.demo import demo
    
example_portfolio = [{"name": "mco", "number": 1.0}, 
                     {"name": "goog", "number": 0.5}]
depth = 5
print(demo(example_portfolio, depth=depth))
```

## Instalation

```sh
python3 -m pip install git+https://github.com/Jabca/EconomicApi
```

### Packages

- yfinance - stcok prices history
- pandas - data analysis
- pandas_datareader - benchmark history
- pytest - unit tests
- pyqt5 - gui
- requests_cache - requests cache for gui

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
