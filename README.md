#eva

Eva is a fork of Sean Brant's virtualenvwrapper.configvar project. The main difference is eva looks for the .env file in your project's folder as specified by the -a flag. It also has the **eva** command that will show you a table of the variables from the .env file and what is actually set in the environment.

##Install

Eva should be installed outside of a virtualenv in your root site-packages.
```
pip install eva
```
Use _**sudo**_ if your current user does not have permissions to install globally.

```
>>>sudo pip install eva
```

##Usage

####Make sure you have a .env file your project folder
```
>>>nano /your/project/path/.env
```
#####File Format
```
SECRET_KEY=ADFDAFJKADFLDSKJA
DATABASE_ENGINE=mysql
CACHE_ENGINE=redis
```

####Create a virtualenv with a project folder using the -a flag.

```
>>>mkvirtualenv <your_env_name> -a /your/project/path/
```

####Make sure your environment variables were set

```
>>>eva
List of Environment Variables from .env file
+-----------------+-------------------+-------------------+
| Key             | Value             | Environment Value |
+-----------------+-------------------+-------------------+
| SECRET_KEY      | ADFDAFJKADFLDSKJA | ADFDAFJKADFLDSKJA |
| DATABASE_ENGINE | mysql             | mysql             |
| CACHE_ENGINE    | redis             | redis             |
+-----------------+-------------------+-------------------+
```

#####Table Legend
**_Key_**: The name of the environment variable as set in the .env file and in the environment.

**_Value_**: The variable's value as specified in the .env file.

**_Environment Value_**: The actual value of the variable in the environment