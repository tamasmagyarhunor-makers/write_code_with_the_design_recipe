# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

```
As a child
So that I can store my toys
I want to put toys I've played with to my toybox and see a list of them.
```

```
potential objects:
- ToyStorage
- Toy
- ToyBox

potential functions/behaviours/features:
- add toys
- see number of toys
- see type of toys
- toys list
- retrieve toys
- toys played with
- remove toys
```


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class ToyStorage:
    def __init__(self):
        # Properties:
        #   toy_list: List
        # Side effects:
        #   sets toylist to an empty List
        # Returns:
        #   nothing

    def add_toy(self, toy):
        # Properties:
        # toy: string
        # Side effects:
        #   adds toy to the self.toy_list
        # Returns:
        #   nothing

    def see_toys(self):
        # Properties
        #   None
        # Side-effects:
        #   None *(but it returns the self.toy_list)
        # Returns:
        #   returns the self.toy_list
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a new instance of ToyStorage
It comes with an empty list (self.toy_list)
"""
toy_storage = ToyStorage()
actual = toy_storage.toy_list
expected = []
assert actual == expected # => []

"""
Given I add a toy to the toy_list
I want to see the toy in the toy_list
"""
toy_storage = ToyStorage()
toy_storage.add('teddy')

actual = toy_storage.toy_list
expected = ['teddy']
assert actual == expected # => ['teddy']

"""
Given I add two toys to the toy_list
I want to see both toys in the toy_list
"""
toy_storage = ToyStorage()
toy_storage.add('teddy')
toy_storage.add('ball')

actual = toy_storage.toy_list
expected = ['teddy', 'ball']
assert actual == expected # => ['teddy', 'ball']

"""
Given I add some toys to the toy_list
I want to see all toys in the toy_list
"""
toy_storage = ToyStorage()
toy_storage.add('teddy')
toy_storage.add('ball')
toy_storage.add('barbie')

actual = toy_storage.see_toys()
expected = ['teddy', 'ball', 'barbie']
assert actual == expected # => ['teddy', 'ball', 'barbie']
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
