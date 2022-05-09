# Scuffed_Wordle
Final project for Programming 1.

## Description

This README is a visual presentation for what I have acomplished with my final project in Programming 1.
This program is a scuffed wordle game with colored prints that you play in the vscode terminal.
You get to pick the difficulty: 3, 4, or 5 letter words.

## Languages

- Python

## Requirements/Prerequisites

- Python 3.7+
- colorama library

## Installation

Exempel 1: 

1. Clone repo
```cmd
    git clone https://github.com/CrazyChr1504/Scuffed_Wordle
```
2. Install colorama
```cmd
pip install colorama
```

## Usage

```
for words in ui_list:
    counter = 0
    ic  = 0
    for letter in words:
        if letter in letter_list:
            if words.count(letter) > letter_list.count(letter):
                x = words.count(letter)
                counter += 1 
                if (counter + 2) == x:
                    if letter == letter_list[ic]:
                        print(Fore.GREEN, f"{letter.upper()}", end="")
                    else:
                        print(Fore.YELLOW, f"{letter.upper()}", end="")

                elif counter < x:
                    if letter == letter_list[ic]:
                        print(Fore.GREEN, f"{letter.upper()}", end="")
                    else:
                        print(Fore.YELLOW, f"{letter.upper()}", end="")

                elif counter == x:
                    print(Fore.WHITE, f"{letter.upper()}", end="")

                else:
                    print(Fore.WHITE, f"{letter.upper()}", end="")

            else: 
                if letter == letter_list[ic]:
                    print(Fore.GREEN, f"{letter.upper()}", end="")
                else:
                    print(Fore.YELLOW, f"{letter.upper()}", end="")

        else:
            print(Fore.WHITE, f"{letter.upper()}", end="")
        ic += 1
    print(Fore.RESET, "")
```

## To do/Roadmap

- [x] README.md
- [ ] Better word checking
- [ ] More languages
    - [x] English
    - [ ] Swedish

## Changelog

### Version 1.0.0

- Working code for three letter wordle.

### Version 1.0.1

- Working code for four and five letter wordle.
- Changed seperate code for each difficulty into one function.
- Bug fix: multiple colored prints on letters that were showing more than needed.

### Version 1.0.2

- New function to add more words in each word list.

## Contribution

As the assessment has not yet been graded, no pull requests are allowed. As soon as an assessment has been graded, this will be allowed.

In the event of major changes, I would like an issue to be opened up for discussion about what should be changed.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact

Ditt Namn - Christopher Christensen chris95504@gmail.com

Projektlänk: https://github.com/CrazyChr1504/Scuffed_Wordle/

## Acknowledgments

- Niclas Lund
