# Mars Lander Game
Mars Lander Game based on pygame library.

## Introduction:
The Python pygame package is an Open Source library for making multimedia applications and games. It is
built on top of the excellent SDL library, and like that library it is highly portable and runs on nearly every
platform and operating system.
pygame home page:
https://www.pygame.org

## Documentation, including tutorials and sample code:
https://www.pygame.org/docs/
pygame is excellent for reproducing classic arcade games from the 1970s and 80s, and it has been used to
recreate Pong, Pacman, Snake, Defender, and Asteroids amongst many others.
We introduced pygame in CS1527 Practical 8 and you are urged to study the sample programs and exercise
solutions before starting work on this mini-project assessment.

## Background:
One of the first arcade games to be based on a real space
mission and using pseudo-realistic physics was Lunar
Lander (Atari, 1979).
In the game, players control a space vehicle as it makes its
approach to the surface of the moon. By pressing various
keyboard keys, the vehicle can be rotated right or left, or
the main rocket engine fired (to decelerate the vehicle).
Fuel is limited, so the player has to carefully manage use
of the main engine. Points are scored by landing on various
landing zones, but the vehicle must have horizontal and
vertical velocity below certain acceptable limits or it is
destroyed. Similarly, attempting to land outside a landing
zone results in a crash. A successful landing triggers an award of points, and a new landing
mission (with landing zones in new, random locations).


## 1.	Mars Lander
This mini project was all about creating an updated version of one of the first arcade games to be based on a real space mission and using pseudo-realistic physics. It is called Lunar Lander by Atari and was launched back in 1979. 
Mars Lander game was designed and built using the Python pygame package which is an Open Source library for making multimedia applications and games. It was pretty challenging and required to bring all the knowledge and skills one has acquired during the CS1527 course. However, it was all fun and worth the effort kind of experience which I believe motivated me and vastly expanded my knowledge in the field of Pygame and Python.

## 2.	Description
The player begins with 3 ‘lives’, with the lander positioned at the top of the screen with random vertical and horizontal velocities. It also has 500 kg of fuel being reduced by 5 every time the main engine thrust is fired (‘space’ key). Whenever the lander goes beyond the right or the left of the screen it wraps onto the opposite side of it. Besides, the Mars lander is not allowed to fly off the top of the screen.

At the top left hand corner of the game window the user is provided with instrument panel which displays the changing time, altitude, fuel reserves, velocity (x, y), damage sustained and lives left. The player’s main goal is to successfully land on one of the three landing pads placed on different locations on the Martian surface. Proper land adds up 50 points to the total game score which the user should aim to increase as much as possible. Furthermore, “You Have Landed Successfully! +50 pts” message is shown on the screen while the program is paused and waits for a key press.
Each time the lander starts with 0% damage which instantly jumps to 100% in case the lander reaches the bottom of the screen or a hard landing occurs. This results in a “You Have Crashed!” message being displayed on the game screen and costs the player 1 life and the game pauses till a key is pressed.

Moreover, the Mars lander’s velocity (y) is incremented by a small amount every game cycle in order to introduce the acceleration due to gravity effect.
There are random control failures which occur for a duration of 2 secs preventing the player from using one randomly chosen control feature of the lander. The user is notified by the “*ALERT*” message displayed at the bottom left hand side of the instrument panel. 
The program also demonstrates 5 fixed position obstacle sprites which cause 10% damage to the lander when hit which destroys them (makes them invisible). It also displays random meteor storms consisting of 5 to 10 meteors every one of which dealing 25% damage to the Mars lander. If the lander sustains 100% damage (meteors and/or obstacles), all the controls are disabled (resulting in a crash). 

If one wishes to exit the game he/she can do so by pressing the ‘Esc’ key or by clicking the red ‘X’ button.

## 3.	Testing
The aim of testing is to make one understand more about the program or application under test. For this project I used the Bottom-Up testing approach to ensure it’s doing what I intend it to do. I ran the program every time I implemented a new feature in the code to analyze the output. It was the clearest and easiest way for me to check for errors. One of the main advantages of this approach is that it offers easier observation of test results. Besides, it does, indeed, have some disadvantages but at the end of the day it helped me reach my goal and understand how the Pygame package behaves. 


References: https://www.pygame.org/docs/, https://stackoverflow.com/
