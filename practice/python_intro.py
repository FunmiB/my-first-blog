print('Python scripting: Day 1 \'May-25-2024\'')
BUILDING_BLOCK={'DNA':['A', 'T', 'G', 'C'], 'PROTEINS':['Met', 'Val', 'Ala', 'Leu', 'Ile', 'Phe', 'Pro', 'Gly', 'Trp', 'Tyr', 'His', 'Asn', 'Gln', 'Thr', 'Ser', 'Glu', 'Asp', 'Arg', 'Lys', 'Cys'], 'RNA':['A', 'U', 'C', 'G']}
print(BUILDING_BLOCK['DNA'])
print('-'*20)
print(BUILDING_BLOCK['PROTEINS'])
print('-'*20)
first=BUILDING_BLOCK['DNA'][0] 
second=BUILDING_BLOCK['DNA'][1]
third=BUILDING_BLOCK['DNA'][2]
start=first + second + third
print('Transcription')
print()
print('Translation')
print(start)
print('-'* 20)
print('We made a protein, Methionine.')
