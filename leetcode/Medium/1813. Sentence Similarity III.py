def verifica(sentence, vetor):
    cont = 0
    # print("Sentença base:", vetor)
    # print("sentença que busca:", sentence)

    for palavra in vetor:  
        index = sentence.index(palavra)
        
        if (index == 0):
            sentence[index] = 0
        else:
            # print('anterior', sentence[index-1])
            # print('atual', sentence[index])
            if not str(sentence[index-1]).isdigit():
                if cont != 0:
                    cont += 1

                sentence[index-1] = cont
                cont += 1

                if cont > 2:
                    raise Exception()
                sentence[index] = cont

            else:
                sentence[index] = cont
        # print(sentence)

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        sentence1 = sentence1.split()
        sentence2 = sentence2.split()

        if sentence2[0] != sentence1[0] and sentence2[-1] != sentence1[-1]:
            return False

        tam1 = len(sentence1)
        tam2 = len(sentence2)
        

        try:
            if tam1 < tam2:
                raise Exception()

            sentence = sentence1[:]
            verifica(sentence, sentence2)
                
        except:
            try:
                
                if tam1 > tam2:
                    raise Exception()
                sentence = sentence2[:]
                verifica(sentence, sentence1)
                
            except:
                try:
                    sentence = sentence1[:]
                    sentence = sentence[sentence.index(sentence2[0]):]
                    sentence[0] = " "

                    verifica(sentence, sentence2)
                except:
                    return False
            
        return True
