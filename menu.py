import Light
import grovepi

__author__ = 'adilettad'


print("---------------")
print("----Welcome----")
print("------to-------")
print("-----Saber-----")
print("---------------")

sab = Light.Saber()
command = input("Command:")
if "blink" in command:
    sab.blink

