# Weather Module

This is a small script written in python to add a weather module in your status bar. I use it in my [polybar config](https://gitlab.com/sourin0903/dotfiles/-/tree/master/.config/polybar) .

## Dependencies :

 1. python :
   * requests.
   * json.
 2. [Openweather](https://openweathermap.org/) API key.
 3. [weahter icons font](https://erikflowers.github.io/weather-icons/).

## Installation Guide :

### General Installation:

 1. Clone this repository using the command : ```git clone https://github.com/SoumavaSeal/weather_module.git```

 2.  cd into the directory. ```cd weather_module```

 3. create a new file named credentials.py. ```touch credentials.py```

 4. write city name and your api key inside the file.

  ```python
  city = "${your_city_name}" # replace your_city_name by the name of your city (say, "bangalore")
  api_key = "${your_api_key}" # replace your_api_key with your openweather api key.
  
  ```

### Additional steps for Polybar Installation :

 1. copy this folder to the polybar config folder. Typically it is located in `~/.config/polybar/`.

 2. Add a custom module in polybar and give actual the path of `icon.py` and `data.py` in the `exec` field of the module to get the icon and temperature of the day.


 **Note :** _In order to have the weather icons you have to install the [weather icons](https://erikflowers.github.io/weather-icons/). For arch based distributions it is available in the AUR as **[ttf-weather-icons](https://aur.archlinux.org/packages/ttf-weather-icons/)** package_
