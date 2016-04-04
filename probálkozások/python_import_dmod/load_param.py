import argparse


parser = argparse.ArgumentParser()
parser.add_argument("pFile", type = str, help = "Modules")
args = parser.parse_args()
pFile = args.pFile[:-3]

print pFile

modules = map(__import__, [pFile])

print modules

parMod = modules[0]

params = parMod.parameters

print params
