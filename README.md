[Volume 1: O Manual de Referência](https://www.amazon.com.br/dp/B0FJ1HYJN8)

[Volume 2: Construindo Aplicações Gráficas](https://www.amazon.com.br/dp/B0FLJ8PNYJ)

[Lucida-Flow Support - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=SoteroApps.lucidaflow-support)

[Lucida-Flow - pypi org](https://pypi.org/project/lucidaflow)

[Sponsor](https://github.com/sponsors/marconeed)

______________________________________________________________________________________________

## Using the Terminal:

Note:

Download the Lucida-Flow repository into a folder using the Windows terminal or VS Code terminal:

```
git clone https://github.com/marconeed/Lucida-Flow
cd Lucida-Flow
```

Note:

Download the dependencies using the Windows terminal or VS Code terminal:

```pip install requests```   

Note:

To create programs with a graphical interface, we need to create 2 files:

The .py file containing the code to draw the graphical interface.

The .lf file containing the program's logic code.

Both files need to be in the root of the programming language folder, where all the language code is located, or you can place them in other locations, but you will have to reference the folder paths for the imports that both files need to work.

The language contains GUI codes used in the book, located in the project's root inside a folder called gui. Just place the ones you will use in the root next to the .lf file. If you want to leave them where they are, you need to change the import paths in both files.

Note:

To execute, simply run this command using the Windows terminal or VS Code terminal in the folder where the files are located, and remember to reference the .lf file inside the

```python main.py nome_arquivo.lf```

```python nome-do-arquivo-gui_host.py```


## Using VS Code:

Note:

Download the language extension for VS Code:

```https://marketplace.visualstudio.com/items?itemName=SoteroApps.lucidaflow-support```

Note:

Download the dependencies using the Windows terminal or VS Code terminal:

```pip install requests```   

Note:

The extension helps in building the code with suggestions and syntax highlighting (underlining the words), making it much better to program in VS Code.

VS Code supports running the `.lf` code directly in it, but for graphical interface programs, you will have to use the VS Code terminal to run the execution command. The command is the same: ```python filename-gui_host.py```


## Using pypi.org:

Note:

Download the language from pypi.org:

```https://pypi.org/project/lucidaflow```

```pip install lucidaflow```

Note:

By using the language this way, you eliminate the need for the language files to be in the same folder to work. Just create an empty folder with the `.lf` file and run it, or `filename-gui_host.py` + `.lf` and run it if it has a graphical interface. To execute, the command is ```python -m lucidaflow filename.lf``` or ```python filename-gui_host.py```.

Using it this way combined with VS Code and the extension helps in building the code with suggestions and syntax highlighting (underlining the words), making it much better to program in VS Code.

To execute in the Windows terminal, simply open the Windows terminal in the folder where the `.lf` file is located and type ```python -m lucidaflow filename.lf```, or open the Windows terminal in the folder where the `gui.py` is located and type ```python filename-gui_host.py``` if it has a graphical interface.

To execute in VS Code, simply press play for `.lf` files. For `.lf` and `gui.py` files, you must use the VS Code terminal: ```python filename-gui_host.py```.


## Activate the REPL (in any folder on your computer):

Turn your language into a professional command-line tool:

```python -m lucidaflow.cli```

_____________________________________________________________________________________________________________________________________________________________________________

## Support the Project

Lucida-Flow is an independent, open-source project. If you like the language and want to see its development continue, consider [tornar-se um patrocinador no GitHub Sponsors](https://github.com/sponsors/marconeed)! Your support is fundamental for the maintenance and evolution of the project.
