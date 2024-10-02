from collections import Counter

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        tam = len(s)
        
        vet = [i for i in range(tam, 0, -1)]
        maior = 0
        
        for i in range(tam, 0, -1):
            for j in range(0, i):
                palavra = s[j:i]
                count = Counter(palavra)
                dist = len(palavra)
                if (count['a']%2 == 0):
                    if (count['e']%2 == 0):
                        if (count['i']%2 == 0):
                            if (count['o']%2 == 0):
                                if (count['u']%2 == 0):
                                    if maior < dist:
                                        maior = dist
                                    
                                    if 1 not in vet[maior-1:]:
                                        return maior
                                    
                                    
                vet[dist-1] -= 1

        return maior
                    
solu = Solution()

print(solu.findTheLongestSubstring("lffjsdhuyanjfesetkrgdkvpgjtwzbwtgfkvqggundksswifayuwwqjmrmmckkeiitofogmpcyowdrfijnjxzjgluwevtygrudzngiyrrvuhevzsvczkbxyoiuwbvbthbxlcfvfggzutbqttwuqavnpyubrhqhvdknfbqtmjlaokmopplxufnbvwqkisbamepgmrtxofhqbtfnoxsuxagbstmcwqmaezhwmkgdumkbtcgllwbunsjnjuqfxfzqsevwasangzhodanfrjqxoxvfztsmgzzwjkdudrdpbzrmlrbdoibskxoejobejrdzsducnnqcnlrsfwsppwuwtqynjyoohgszrgebixayoovfgjrjecfqcvffnfgynzikyverhnkxyayyxxhfujbdhtvansaqbfvztazroxxnuelmhyvspwruidqxjajuqybjbclldvqoiwbbriklhyizpiyychnmpftnonhoyqucxqmmggtebueollzzvzdihkjavinoiukzwwcwxainwehtltmyahrwxfhvdgdgxuhbnxkexvaoutgbtzbwydbglcmstgvkmjftjjislhhdxmeljltqslbqbcnkqlrhjqjmqrkferdvtevhwjnniqutzvuljoobornasdjtqfucdhlolvjeiyvdxezvpkrhlbbdfpovqcmbsxecjautohtzxhgwersmesweflvblaxvvpocbwwozemuiybbqbfhtxjqdysjfbsdpeyidrzcvkezhhksozlsywvascxisrfaxruyltjrfuaprflszqlwyrnpplndvcdzhzkgbwztswbslhyytznmbvbnyzxsyivslwcdkflmofxfnwpgaqxfgvufvctxxttacgoibzminxhodcgggafnupokfvgncmwllcqvoqvrwagillaghnklvtoowxxdxrybugykcniwvyhbjdjseznlqczjcopfhsaragzgktcsmnqzumvskmojqlgerujrdxplmwfvbcpvbmesxefqcxmrgqmylwsnfnsihyxsltqazzywjjqyiegyobzyidxvcbuucpepotmhvbnfbjobequugguwfgeamuaymtllkekkrwkubkoyyfcaxapvdgmtqntdiqnbzyogbrawxjncklsmbtviegafobtsznwdrbqfwuvuocaraeharbqusvhtwnwdplkfxvghcugfwjccwgexcoyyilhefsyhnclqrfybyrvbiarxspngszdlwkqqsxtyvyifxsjzjpqkqutndbccjtnumlkscwersxoqnhrzixnkujfbdxdodxpywlidkmdfqxroxzqcpksdkdydrhphpkbfbanvkjrtxhlevyxycugybfyywlnvigfgmyqffhoettytyjskfvkrstjhzgfjbeeanblwoengfrlxfxcwilkbqjvextpubzouyntcaaybaayglgobwbhjgryfgsglrgxeswdkfrzuovparpcaoksllnewddovzkfucmaqoavytejzijbppbsezaptnbhdxmvrqasjaahqwumiulxagtxngxoqybezrtiubdmdbptpedwpifbdrocfkoyrfwpxliwyjpfvjqafhdxmcdjzzwdivhfyvldodkqrcosncqtdotpimopmmdmkzuwacfpnacxmvqtkbyaquaoxqfojwncqxtgnkpynumvuaswxqurdfymrzeigpxekxxrudftwuzpajbvrdipxfniljkifqsgttrdtfidgbvveqyusyvuxvoxurdrryhfnntyfbkwzakywfelhvsbwzxnufksguhpjisuqqwsyqphyyfwcshoemfawdxbbrbtpyoxapijixmpdcjumnghqecwwxjgzdlyiehllfxyddxgjhucbktxmgltvwcyookvjkvyqaqcefaahgywvxxnjufdmqqatgcgfkgyzxkzhilmwkbogyvdoemmgkkhpomxaoluupkbomvtwsvppwvjbqohcujufogifrjxmagstpajuxyizricymbsrwbgwpygmkjptqiwzitfmmpzrhhntocwymbawglgdwbpgbvfkbvqiggznqcsfibeawyzbsrgxfkefwmsyaaskquyagcyxpocfiqaznjsrsgfkdxsjwjgsqdaiggyhrgpkmztpxdlcoipxbakpwahrebmdhbjtlddiixehrxtepbnowaakunjpbxoknuafilhcetwkmrrswjyqyklzpetgngdycfauacoqscflqzruffxncodapyulmxeslethmkgzqyurdjogsvoeibfgwprgbmulpqnhgyucaezptwgpimdqcdlfgvnjniyquhmnbbxxglmkyniowmfewnlwvlsylqnblydkbgxtlfrysxjprfnllafftlzwwpuovrgdkuxanhojnicrgodubywaryshhbtpvkggdawyjuiwdelonkzywbqjcohfsssgqjysuspjvidruiffqxtfnwjmmhfnfrrkhgyejwvcucwhdujyaemmubdtbeomjhfphushtiqynzosswjeuvqzebeuresaqirrfwblprztfhkuyufwgvfzspvxhegbqkzhmowiwfdbcbjpbdujztlzlhgigfkivxklbcgfmuogtaommlvlpttauixczvbmnlzwmfjugytcjanboamgrtpziatwxghvueytwkzhuikbmjauoanadfvhamtoeycggynsswllcxzhgdetilwxkninlvhcozhuiuaqtkglsvjlwgvlkrrincmgxoxsggkpoabjeqmcjrsekkmpuvseihhmwslttrxbjoqwluaeppyabmuwnxdgvnxlnomncpfqvgfdxnzlhfmwslwtlervfzzhirhuzczcgsnpybkhcnckfzphlxssgzjfoyxydvadirjzdxjgoxhxanyckoooruhnimtcsmvmddlyllmppgugzezgdxaswfpkijcgywtyrezviwhdsyjqnksrleqoqhukgrxkeremwjbawbnlbqosxvouqjrmmvykipcazekculbbumkgenhjkahgimjpmpytoyiaoooqnxztgtlunffvszorltqagxdlxbuwockudcqlhwckehlhihqmsbaiyxipdpvnidblplrtignxmfsyulcrojpxlgkmylfolirxehxfkvwadegerqbmyeekpodamemcxtecqijesxxkvwdsocqyuagqylwodgaszazvrdjuvanurfrttixfbasggfxwdulbvwvvjdtfgabhfnsheaqopbepiorywlsktvonhxloppagkgdkobywfivrhowneyfszbqskpxvwjriiqqmhqhkjisksmihttcupfzyylrvsfrtcopvlkcrqghvwelkrqqrffuygsggrbsungonkvakfehnrpfqddsdatofcrcewanzigluouypzotpousidkkcosvmimkcjeiuvaefftmdhmfwjltqemdtmlhadgwymcasllmdetyfggohqfoiphmaadfbhkkdnpeubislwgrkpejxjalpaytzhhbrvrjfpjrcgdfsakeqxexbgfhevhruhhwxsjqtnhxsemsvvxsyevfmmqevdsqergvfphpckbpeoeqyrmmdzafgtshitmibbpoucyynengtaaixahewgvpsiufqxgilmtazymycrxnjajdgpdluhvtftaummsbfureuiptxmedlxothitffouogmucgwznfobcbveengtmqdknzvzzysmjwgnbbykimpjckyzsebcbfpknxbodxpigmfnhxlmywdwptmkzuxxuvhbcixbsgngrtxgbcjuyctaqvzayvzeofbubuyhhgraohnhuelbqrlnbzlxahpsmgwpiflujdazsqrmrmtssudexfiulbyzjgmuucobevbeeofefsekshtdlidbfdbtywhbjerawvfobnadfcbzbkptozixprdqzvrzthhjyrnpajyswpogxvmefzfckgpwadkxzaqktvhzegtqlgxkfynowfmllyjigzldltvwfxseifqqishhuoguviviuvpkfljauaqtmynjwleevsdcsstcydfhlbhlnnyriomuzaxrvwlyyowsmclsudlojdnyjzvpnoegzltxgmeqkbfqdcutwgaupzkpnftkxhbyjcabavxohtkktkdejziuyzrctmkpukfsjbjznarrtgeyvdxrsoyikddlnxuonmbtrkadgmhwjpnvlmoonczsjpjpcevcdvuxqmyfylyfcnqahzynsfqcobglkdehuapfpjgsiztsiobjkcpopbloplalgwzeccjnnkivvqvidmhxcpzefrqrlhjcyyfolyzogmbjiakufyjytmjgjwylwpjvixougyggjmbzarudlmlyhvcxbhuqurxlznwkkrjbyiioumtsmybrtzvibqyvhibxmvgkoiyzmjdrq"))