# Todo App

This program manages ToDo items. 

## Classes:

### ToDo_Item 

#### Attributes:
* `name`
* `is_done`

#### Methods:

##### `__init__`

Parameters:
* `name`

##### `mark`
Change status 'is_done' for True

##### `__str__`
Display in proper format {[ ]} {name}

##### '__eq__`
Compare equal two objects


### ToDo_list

#### Attributes:
* `list_of_items`
* `title`

#### Methods:

##### `__init__`

Parameters:
* `title`

##### `Add item`
Add item to list.

##### `Mark item`
Mark item in list.

##### `Archive`
Remove complited (mark) tasks.

##### `Show all items`
Display items from list.

##### `Create from csv`
Get data from file and create proper objects

##### `Save to csv`
Save data to csv file

## Controller
Manages all object's methods.

## Main
Run application.

## View 
Manages all prints, inputs and look.

