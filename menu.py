import Light
import grovepi

__author__ = 'adilettad'


print("---------------")
print("----Welcome----")
print("------to-------")
print("-----Saber-----")
print("---------------")

sab = Light.Saber()
command = raw_input('Your command:')
if command == "blink":
    sab.blink

