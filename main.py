from df_generator import *


def main():
    print('Single molecule BRICS fragments:\n')
    generator = FragGenerator()
    generator.showFrags()
    generator.getFragments()

    print("\nBRICS generation...\n")
    brics_generator = Brics()
    brics_generator.brics()
    brics_generator.buildBrics()
    frags = brics_generator.newBrics()
    print('Done!')
    print('\nGenerating the DataFrame with the descriptors...: \n')
    dfgenerator = DfGenerator(frags)
    dfgenerator.output()

    print("\nCompleted! Check your results!")


if __name__ == '__main__':
    main()
