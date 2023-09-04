import PrepareChain
import GenerateText

f = open("data.txt",encoding="utf-8").read()
chain = PrepareChain.PrepareChain(f)
triplet_freqs = chain.make_triplet_freqs()
chain.save(triplet_freqs, True)

def run():
    try:
        return GenerateText.GenerateText().generate()
    except:
        return False

if __name__ == '__main__':
    run()
