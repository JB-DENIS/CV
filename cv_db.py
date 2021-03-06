# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 09:26:15 2021

@author: JB
"""

import streamlit as st 
import streamlit.components.v1 as components
from PIL import Image 




### Chargement des images :
    
img_size=(150,150) 
icone_img=Image.open('img/profil.jpg')
profil_img=Image.open('img/profils2.png')
bar_img=Image.open('img/bar.jpg')

comp_duo=Image.open('img/comp_duo.jpg')
comp_ico=Image.open('img/comp_ico.jpg')

form_road=Image.open('img/form_road2.jpg')

exp_data=Image.open('img/exp_data.jpg').resize(img_size)
exp_chimie=Image.open('img/exp_chimie.jpg').resize(img_size)
exp_open=Image.open('img/exp_open.jpg').resize(img_size)
exp_data_oc=Image.open('img/exp_data_oc.jpg').resize((240,180))
exp_sc_broyeur=Image.open('img/exp_sc_broy.jpg').resize(img_size)
exp_sc_four=Image.open('img/exp_sc_four.jpg').resize(img_size)
exp_sc_laser=Image.open('img/exp_sc_laser.jpg')
exp_sc_bat=Image.open('img/exp_sc_bat.jpg')
exp_sc_enz=Image.open('img/exp_sc_enz.jpg').resize((40,80))
exp_diver_maison=Image.open('img/exp_diver_maison.jpg')
exp_diver_cart=Image.open('img/exp_diver_cart.jpg').resize(img_size)
exp_diver_jap=Image.open('img/exp_diver_jap.jpg')

interet_mot=Image.open('img/interet_mot.jpg')

publi_brevet=Image.open('img/publi_brevet.jpg')
publi_poster=Image.open('img/publi_poster.jpg')
publi_these=Image.open('img/publi_these.jpg')
publi_prix=Image.open('img/publi_prix.jpg')

media_cv=Image.open('img/media_cv2.jpg')
media_lm=Image.open('img/media_lm.jpg')
media_lr=Image.open('img/media_lr.jpg')
media_git=Image.open('img/media_git.jpg')
media_linkedin=Image.open('img/media_linkedin.jpg')

glob_comp=Image.open('img/glob_comp2.jpg')
glob_int=Image.open('img/glob_int.jpg')
glob_exp=Image.open('img/glob_exp.jpg')
glob_form=Image.open('img/glob_form.jpg')
glob_kw2=Image.open('img/glob_kw3.jpg')

media_yt_f = open('video/YT.mp4', 'rb')
media_yt = media_yt_f.read()

#st.set_page_config(layout="centered")
st.set_page_config(page_title='CV JB DENIS',layout="wide",page_icon=icone_img)

### Pages
  
def page_accueille() : 
    st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)    
    st.markdown("<h1 style='text-align: center;'>Bienvenue sur mon CV interactif</h1>", unsafe_allow_html=True)

    st.info(' Dans le menu d??roulant _***Navigation***_ de la sidebar, choisissez une cat??gorie pour acc??der au contenu.')  
   
    st.subheader('_**Aper??u du contenu :**_')
    
    col1, col2, col3  = st.beta_columns((2,0.2,2.8))
    col1.subheader('Comp??tences')
    col1.image(glob_comp,use_column_width=True)
    col3.subheader('Exp??riences')
    col3.image(glob_exp,use_column_width=True)
    
    col4, col5, col6, col7, col8 = st.beta_columns((3,0.00000001,1.1,0.2,1.4))
    col4.subheader('Int??r??ts')
    col4.image(glob_int,use_column_width=True)
    col6.subheader('Formations')
    col6.image(glob_form,use_column_width=True)
    col8.subheader('Keywords')
    col8.image(glob_kw2,use_column_width=True)

    return option
   
                 
def page_competence  ():
    st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)
    st.header('Comp??tences')
    st.text('')
    st.text('')
    st.image(comp_duo,use_column_width=True)#width=600) 
    st.image(comp_ico,use_column_width=True)#width=600)  

   
def page_formation  (): 
    st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)
    st.header('Formations')
    st.text('')
    st.text('')
    st.image(form_road,use_column_width=True)#,width=900)
    
    
def page_experience():
    st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)
    st.header('Exp??riences')
    st.text('')
    st.text('')
    st.markdown("<h5 style='text-align: center; color: gray;'>Choisissez une cat??gorie</h5>", unsafe_allow_html=True)
    st.text('')
    col1, col2, col3  = st.beta_columns(3)
    col1.image(exp_data,use_column_width=True)
    col2.image(exp_chimie,use_column_width=True)
    col3.image(exp_open,use_column_width=True)
    
    col4, col5, col6, col7, col8, col9  = st.beta_columns((0.5,1,0.5,1,0.5,1))#((0.5,1,0.35,1,0.45,1))
    bouton1=col5.button('Data')
    bouton2=col7.button('Science')
    bouton3=col9.button('Diverses')
    
    if bouton1:
        
        st.text('')
        st.text('')
        col10, col11, col12  = st.beta_columns((2,1,1))
        col10.header('Apprenti Data Scientist')
        col11.text('')
        col12.header('2020-2021')
        
        st.text('')
        col13, col14 = st.beta_columns((3,1))
        col13.subheader('Contexte')
        col13.write('La volont?? de partir en formation Data Scientist vient du constat, fait lors de mes diverses exp??riences professionnelles, que les datas ont investi tous les c??urs de m??tier. La pertinence et la puissance d???utiliser ces datas pour comprendre et pr??dire des comportements sont apparues comme une suite logique ?? mon parcours professionnel et ainsi acqu??rir un nouvel outil polyvalent.')
        col14.image(exp_data_oc,use_column_width=True)
        
        st.subheader('Missions')
        st.write('La formation se d??cline sous forme de 7 projets professionnels utilisant des donn??es terrain. L???environnement mis en place pour ces projets est le language Python et la m??thodologie de travail appliqu??e est la m??thode S.M.A.R.T.')
        st.text('')
        st.write('Exemples de projets r??alis??s :')
        st.text('')
        col15, col16 = st.beta_columns((1,1))
        col15.write('**_Anticipation de la consommation et des ??missions de b??timents_** ')
        col15.write('Utiliser des donn??es recueillies aupr??s d???immeubles de nouvelle g??n??ration afin de mod??liser et pr??dire les consommations ??nerg??tiques et ??missions de gaz ?? effet de serres en fonction du type de b??timent.')
        col16.write('**_Segmentation des clients d\'un site d\'e-commerce _** ')
        col16.write('R??aliser un clustering d???utilisateurs d???un site d???e-commerce afin d?????tablir des actions commerciales cibl??es.')
        
        st.text('')
        col17, col18 = st.beta_columns((1,1))
        col17.write('**_Classification automatique de biens de consommation_** ')
        col17.write('Mise en place d???un outil de classification automatique de produits de consommation en fonction de leurs descriptifs (texte) et de leurs photos (visuel).')
        col18.write('**_Impl??mentation d???une m??trique m??tier pour le secteur bancaire_** ')
        col18.write('Construire une m??trique m??tier pour la mod??lisation d???un score d???attribution de pr??t bancaire, interpr??tation sur Dashboard et d??ploiement de l\'API.')
        
        st.subheader('R??alisations')
        st.write(':black_small_square: Data Mining, Etude statistique')
        st.write(':black_small_square: Pre-processing, feature engineering, r??duction dimensionnelle (ACP)')
        st.write(':black_small_square: Machine learning supervis?? : r??gression, kNN, SVM,  Random Forest, XGBoost, LightGBM')
        st.write(':black_small_square: Machine learning non supervis?? : Kmeans, DBScan, HAC, GMM')
        st.write(':black_small_square: M??trique m??tier, optimisation bay??sienne, stacking')
        st.write(':black_small_square: Deep Learning, NLP (BoW, Tf-IDF, Embedding), visuel (BoVW, CNN, Transfert learning)')
        st.write(':black_small_square: Spark, AWS')
        st.write(':black_small_square: D??ploiement  API, Dashboard ')
        st.write(':black_small_square: Analyse de r??sultats, reporting et vulgarisation ')
        st.write(':black_small_square: GitHub rassemblant tous les projets (Voir **M??dia**) ')
        
        ###
        st.text('')
        st.text('')
        st.text('')
        col19, col20, col21 = st.beta_columns((1,1,1))
        top_but=col20.button('Retour haut de page')
        if top_but:
            st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)
            
    if bouton2:
        
        st.text('')
        st.text('')
        col10, col11, col12  = st.beta_columns((2,1,1))
        col10.header('Ing??nieur de Recherche  Entrepreneur ')
        st.subheader('_Recyclage des moteurs d?????olienne_')
        col11.text('')
        col12.header('2017-2018')
        
        st.text('')
        col13, col14 = st.beta_columns((2.5,1))
        col13.subheader('Contexte')
        col13.write('La production d?????nergie par l?????olien repr??sentait 6.3% du parc fran??ais en 2019 et ne cesse d???augmenter. Cette diversification des moyens de production d?????nergie pose de nouveaux enjeux notamment au niveau environnemental. En effet une seule ??olienne comprend une grande quantit?? de Terres Rares, ??l??ments critiques en fort ??puisement et principalement produits en Chine. Cet enjeu a nourri la volont?? de lancer le projet de cr??ation de la start-up RECUP???TR afin de d??velopper un proc??d?? propre et local de recyclage des Terres Rares contenues dans les aimants permanents d?????oliennes.')
        col14.image(exp_sc_broyeur,use_column_width=True)
        
        st.subheader('Missions')
                                                        
        st.text('')
        col15, col16 = st.beta_columns((1,1))
        col15.write('**_D??veloppement et am??lioration du proc??d?? de production _** ')
        col16.write('**_Gestion de projets / Management d?????quipe technique _** ')
        
        st.text('')
        col17, col18 = st.beta_columns((1,1))
        col17.write('**_Entrepreneuriat_** ')
        col18.write('**_Etude de march?? et profils clients (Datas BPI France)_** ')
        
        st.subheader('R??alisations')
        st.write(':black_small_square: Synth??se par broyeur plan??taire, presse, traitement thermique sous H2, Extraction chimique')
        st.write(':black_small_square: DRX, MEB, Granulom??trie, Bobine Supra, ATG, EPMA')
        st.write(':black_small_square: R??daction du mode op??ratoire de production (Enveloppe SOLEAU)')
        st.write(':black_small_square: R??alisation des proc??dures de manipulation et de s??curit??')
        st.write(':black_small_square: Conception et mise en place d???outils techniques')
        st.write(':black_small_square: Rendement tripl?? en fin de mission')
        st.write(':black_small_square: Preuve de concept op??rationnelle')
        
        ###
        st.text('')
        st.text('')
        st.text('')
        col10, col11, col12  = st.beta_columns((2,1,1))
        col10.header('Ing??nieur doctorant ')
        st.subheader('_Optimisation du stockage d?????nergie par hydrog??ne_')
        col11.text('')
        col12.header('2012-2016')
        
        st.text('')
        col13, col14 = st.beta_columns((2.5,1))
        col13.subheader('Contexte')
        col13.write('La production d?????nergie est devenue un enjeu majeur de notre ??poque, et la mont?? des ??nergies renouvelables offre de nombreuses possibilit??s. Diff??rentes th??matiques de d??veloppement dans la cha??ne de production s???ouvrent alors et notamment la probl??matique du stockage de cette ??nergie. Le vecteur ??nerg??tique hydrog??ne permet une alternative ?? l?????lectricit?? et exploite de nouvelles technologies avec un impact environnemental r??duit. Cependant ces techniques sont encore jeunes et co??teuses. Dans cette optique, les travaux r??alis??s au cours de cette th??se se sont focalis??s sur la diminution des co??ts de production des mat??riaux de stockage de l???hydrog??ne et sur l???optimisation du proc??d?? d\'??laboration. ')
        col14.image(exp_sc_four,use_column_width=True)
        
        st.subheader('Missions')
        st.text('')
        col15, col16 = st.beta_columns((1,1))
        col15.write('**_M??tallurgie, caract??risations physico-chimique _** ')
        col16.write('**_Manipulation de Gaz en zone ATEX _** ')
        
        st.text('')
        col17, col18 = st.beta_columns((1,1))
        col17.write('**_Gestion de projets, r??unions, plan d\'exp??rience, cahier des charges_** ')
        col18.write('**_Conception bancs essai et outils techniques, maintenance_** ')
        
        st.subheader('R??alisations')
        st.write(':black_small_square: Elaboration d???alliages en four ?? induction ??? Frittages. M??tallurgie, Hydrure sous pression ')
        st.write(':black_small_square: DRX, MEB, EDX, EPMA, DSC, mesure PCT, cyclage')
        st.write(':black_small_square: Mod??lisation des lois de pr??diction de volume de maille d\'un alliage quinaire')
        st.write(':black_small_square: R??alisation d\'un abaque PCT sur l\'utilisation d\'Al et Si dans un syst??me TiVFe')
        st.write(':black_small_square: Proc??dure d\'??laboration optimis??e')
        st.write(':black_small_square: Manuscrit de th??se - Rapport sur les Energies (Voir **Publications**)')
        st.write(':black_small_square: **1er Prix Pr??sentation de th??se** (Voir **Publications**)')
        
        ###
        st.text('')
        st.text('')
        st.text('')
        col10, col11, col12  = st.beta_columns((2,1,1))
        col10.header('Ing??nieur stagiaire  ')
        st.subheader('_Etude environnementale de particules ITER-Like_')
        col11.text('')
        col12.header('2012')
        
        st.text('')
        col13, col14 = st.beta_columns((2.5,1))
        col13.subheader('Contexte')
        col13.write('Le projet ITER sur la fusion thermonucl??aire a pour objectif de produire une ??nergie propre et quasi illimit??e. Cependant la technologie employ??e pose de nombreuses interrogations et notamment sur l???impact humain et environnemental des sous-produits de fusion g??n??r??s lors de l???utilisation du r??acteur.  Dans cette id??e,  il a ??t?? d??cid?? de recr??er en laboratoire et d?????tudier des nano-particules de tungst??ne dites ??ITER-LIKE?? afin d???analyser leurs toxicit??s.')
        col14.image(exp_sc_laser,use_column_width=True)
        
        st.subheader('Missions')
        st.text('')
        col15, col16 = st.beta_columns((1,1))
        col15.write('**_Mise en place et responsable banc d\'essai_** ')
        col16.write('**_R??alisation de nano-particules par ablation laser (ns / ps)_** ')
        
        st.text('')
        col17, col18 = st.beta_columns((1,1))
        col17.write('**_Caract??risation physico-chimique_** ')
        col18.write('**_Formation MEB_** ')
        
        st.subheader('R??alisations')
        st.write(':black_small_square: Production de nano-particules ITER-Like')
        st.write(':black_small_square: MEB, EDS, AFM, granulom??trie')
        st.write(':black_small_square: Rapport pour le projet ITER')
        st.write(':black_small_square: R??sultats envoy??s pour ??tude toxicologique (suite du projet) ')
       
        ###
        st.text('')
        st.text('')
        st.text('')
        col10, col11, col12  = st.beta_columns((2,1,1))
        col10.header('Ing??nieur stagiaire  ')
        st.subheader('_Cr??ation de nouvel accumulateur ??lectrique_')
        col11.text('')
        col12.header('2011')
        
        st.text('')
        col13, col14 = st.beta_columns((2.5,1))
        col13.subheader('Contexte')
        col13.write('Le Projet ROPAS visait la production de batteries flexibles imprim??es sur papier. Afin de s???affranchir des constituants classiques et co??teux d???un accumulateur et r??pondre ?? l???appauvrissement du lithium, le projet avait pour objectif la r??alisation de nouveaux mat??riaux d?????lectrodes organiques (ORB) pour accumulateur fonctionnant aussi bien au Lithium, qu???au Sodium.')
        col14.image(exp_sc_bat,use_column_width=True)
        
        st.subheader('Missions')
        st.text('')
        col15, col16 = st.beta_columns((1,1))
        col15.write('**_Synth??se organique et polym??risation sous atmosph??re inerte_** ')
        col16.write('**_Mise en place et optimisation banc d\'essai_** ')
        
        st.text('')
        col17, col18 = st.beta_columns((1,1))
        col17.write('**_Caract??risation physico-chimique_** ')
        col18.write('**_Formulation et mise en ??uvre d???encre_** ')
        
        st.subheader('R??alisations')
        st.write(':black_small_square: Synth??se organique et polym??risation sous atmosph??re inerte (Bo??te ?? gants)')
        st.write(':black_small_square: Formulation et mise en ??uvre d???encre')
        st.write(':black_small_square: RMN, IR,ATD, ATG, Voltamp??rom??trie, Cyclage d???accumulateur')
        st.write(':black_small_square: Synth??se d\'un nouveau mat??riau ORB')
        st.write(':black_small_square: **D??p??t de brevet** (Voir **Publications**)')
        st.write(':black_small_square: **R??compens?? Prime stagiaire CEA** ')
        
        ###
        st.text('')
        st.text('')
        st.text('')
        col10, col11, col12  = st.beta_columns((2,1,1))
        col10.header('Technicien stagiaire  ')
        st.subheader('_Exp??rience professionnelle ?? Singapour_')
        col11.text('')
        col12.header('2010')
        
        st.text('')
        col13, col14 = st.beta_columns((2.5,1))
        col13.subheader('Contexte')
        col13.write('Dans une volont?? d???ouverture ?? l???International, cette exp??rience professionnelle s???est tenue ?? **Singapour** ?? un poste de technicien sur cha??ne de production d\'enzyme pour le textile.')
        col14.image(exp_sc_enz,width=70)
        
        st.subheader('Missions')
        st.text('')
        col15, col16 = st.beta_columns((1,1))
        col15.write('**_Essais techniques sur banc d\'essai_** ')
        col16.write('**_Contr??le qualit?? produits_** ')
        
        st.text('')
        col17, col18 = st.beta_columns((1,1))
        col17.write('**_Lancement de machine de production_** ')
        col18.write('')
        
        st.subheader('R??alisations')
        st.write(':black_small_square: Reporting, contr??le qualit??')
        st.write(':black_small_square: Echange culturel et linguistique')
        st.write(':black_small_square: Rapport fin de mission ')
        
        ###
        st.text('')
        st.text('')
        st.text('')
        col19, col20, col21 = st.beta_columns((1,1,1))
        top_but=col20.button('Retour haut de page')
        if top_but:
            st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)            
          
    if bouton3:
        
        st.text('')
        st.text('')
        st.text('')
        col10, col11, col12  = st.beta_columns((2,1,1))
        col10.header('Projet c??sure - Artisanat  ')
        st.subheader('_R??novation d???une maison de A ?? Z_')
        col11.text('')
        col12.header('2019-2020')
        
        st.text('')
        col13, col14 = st.beta_columns((2.5,1))
        col13.subheader('Contexte')
        col13.write('Suite ?? mon CDD, je suis devenu??propri??taire d\'une maison datant des ann??es 1930. N??cessitant??de gros travaux d\'am??nagements et de mises ?? niveau, je me suis lanc?? dans sa r??novation compl??te.')
        col14.image(exp_diver_maison,use_column_width=True)
                       
        st.subheader('R??alisations')
        st.write(':black_small_square: R??alisation des gros ??uvres sur chantier') 
        st.write(':black_small_square: Cr??ation d???espaces de vie') 
        st.write(':black_small_square: Mise ?? niveau ??lectrique ??? circuit de plomberie') 
        st.write(':black_small_square: Eb??nisterie') 
        st.write(':black_small_square: Lancement cha??ne YouTube sur le travail du bois (Voir **M??dia**)') 
        
        ###
        st.text('')
        st.text('')
        st.text('')
        col10, col11, col12  = st.beta_columns((2,1,1))
        col10.header('Op??rateur, cuisinier, fermier')
        st.subheader('_Woofing au Japon_')
        col11.text('')
        col12.header('2008')
        
        st.text('')
        col13, col14 = st.beta_columns((2.5,1))
        col13.subheader('Contexte')
        col13.write('Opportunit?? de d??couvrir le **Japon** tout en travaillant dans un centre d\'activit??s.')
        col14.image(exp_diver_jap,use_column_width=True)
        
        st.subheader('Missions')
        st.text('')
        col15, col16 = st.beta_columns((1,1))
        col15.write('**_Responsable stand "Pizza" et stand "Grillade"_** ')
        col16.write('**_Atelier de menuiserie_** ')
        
        st.text('')
        col17, col18 = st.beta_columns((1,1))
        col17.write('**_Accompagnement ??quitation_** ')
        col18.write('**_Travaux de la ferme_**')
        
        st.subheader('R??alisations')
        st.write(':black_small_square: Echange culturel et linguistique')
        
        ###
        st.text('')
        st.text('')
        st.text('')
        col10, col11, col12  = st.beta_columns((2,1,1))
        col10.header('Op??rateur')
        st.subheader('_Vacancier - Int??rimaire_')
        col11.text('')
        col12.header('2007-2009')
        
        st.text('')
        col13, col14 = st.beta_columns((2.5,1))
        col13.subheader('Contexte')
        col13.write('Cha??ne de production d???emballage carton.')
        col14.image(exp_diver_cart,width=120)
        
        st.subheader('Missions')
        st.text('')
        col15, col16 = st.beta_columns((1,1))
        col15.write('**_R??glage machine de production_** ')
        col16.write('**_Mise en palette sortie cha??ne de production_** ')
        
        st.text('')
        col17, col18 = st.beta_columns((1,1))
        col17.write('**_Contr??le qualit??_** ')
        col18.write('')
        
        st.subheader('R??alisations')
        st.write(':black_small_square: Contr??le qualit??')
        ###
        st.text('')
        st.text('')
        st.text('')
        col19, col20, col21 = st.beta_columns((1,1,1))
        top_but=col20.button('Retour haut de page')
        if top_but:
            st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)   


def page_interet():
    st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)
    st.header('Int??r??ts') 
    st.image(interet_mot,use_column_width=True)
    
      
def page_media():
    st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)
    st.header('M??dias')
    st.text('')
    
    cv=('[**CV**](https://drive.google.com/file/d/1oSBKeLdvIjgydBnC_t6o01fb9ucCaomL/view?usp=sharing)')
    lm=('[**Lettre de motivation**](https://drive.google.com/file/d/1hpbAiw7URmtNtQo_BdIHHOX12_Zpb3GC/view?usp=sharing)')
    lr=('[**Lettre de recommandation**](https://drive.google.com/file/d/1UoU_yFMkkjtdxRiluyNAN9NfIWck2mOk/view?usp=sharing)')
    git=('[**GitHub**](https://github.com/JB-DENIS)')
    lin=('[**LinkedIn**](https://linkedin.com/in/jean-beno??t-denis-38000)')
    yt=('[**YouTube**](https://www.youtube.com/channel/UC1i8IXzTvu7rhaXBCLMaDmQ)')
    
    st.markdown("<h5 style='text-align: center; color: gray;'>Cliquez sur un m??dia pour acc??der au contenu</h5>", unsafe_allow_html=True)
    st.text('')
    st.text('')
    
    col4, col5, col6, col7, col8, col9, col10 = st.beta_columns((0.5,1,0.5,1,0.5,1,0.5))
    col5.image(media_cv.resize((125,150)),use_column_width=True)#,width=125)
    col7.image(media_lm.resize((125,150)),use_column_width=True)#,width=125)
    col9.image(media_lr.resize((125,150)),use_column_width=True)#,width=125)
        
    #col4, col5, col6, col7, col8, col9, col10 = st.beta_columns((0.5,1,0.5,1,0.5,1,0.5))
    col5.markdown(cv, unsafe_allow_html=True)
    col7.markdown(lm, unsafe_allow_html=True)
    col9.markdown(lr, unsafe_allow_html=True)    
    
    st.text('')        
    st.text('')        
        
    col4, col5, col6, col7, col8= st.beta_columns((1,0.5,1,0.5,1))
    col5.image(media_git,use_column_width=True)
    col7.image(media_linkedin,use_column_width=True)
          
    #col4, col5, col6, col7, col8= st.beta_columns((1,0.5,1,0.5,1))
    col5.markdown(git, unsafe_allow_html=True)
    col7.markdown(lin, unsafe_allow_html=True)
    
    st.text('')        
    st.text('')
    st.markdown("<h5 style='text-align: center; color: gray;'>Attention, le son est automatiquement au maximum</h5>", unsafe_allow_html=True)
    st.video(media_yt)
    col1, col2, col3  = st.beta_columns((4,1,4))
    col2.markdown(yt, unsafe_allow_html=True)  

            
def page_publi():
    st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)
    st.header('Publications')
    st.text('')
    br=('[**Brevet**](https://drive.google.com/file/d/1RZVpIPAJiq4zO9LPjO2_ahqiKJrSqQ2A/view?usp=sharing)')
    po=('[**Poster**](https://drive.google.com/file/d/1btDY31nkJ-ycOGMaT_ar9SBzTMzDSllW/view?usp=sharing)')
    th=('[**Th??se**](https://drive.google.com/file/d/1-OMgCIu-agnUHLJW8uUhvnJHNP_fdg7t/view?usp=sharing)')
    pr=('[**Pr??sentation Th??se**](https://drive.google.com/file/d/143D5-Euw0HwPIUcxHw49HVQ_j2J1KKZM/view?usp=sharing)')
        
    st.markdown("<h5 style='text-align: center; color: gray;'>Cliquez sur un lien pour acc??der au contenu</h5>", unsafe_allow_html=True)
    st.text('')
    st.text('')
    
    
    
    #col4, col5, col6,col7,col8 = st.beta_columns(5)
    col4, col5, col6, col7, col8, col9, col10 = st.beta_columns((0.5,1,0.5,1,0.5,1,0.5))#((0.6,1,0.9,1,0.9,1,0.9,1,0.0001)) 
    col5.image(publi_brevet,use_column_width=True)
    col7.image(publi_poster,use_column_width=True)
    col9.image(publi_these,use_column_width=True)
          
    col4, col5, col6, col7, col8, col9, col10 = st.beta_columns((0.5,1,0.5,1,0.5,1,0.5))#((0.6,1,0.9,1,0.9,1,0.9,1,0.0001)) 
    col5.write(br, unsafe_allow_html=True)
    col7.write(po, unsafe_allow_html=True)
    col9.write(th, unsafe_allow_html=True) 
    col5.write('_Polym??re comme mat??riau d\'??lectrode pour des batteries secondaires au lithium._ R??f : **WO 2013156899 A1**')
    col7.write('_Influence of impurities on the performance of metal hydride_. MH2014, Manchester, UK, 2014.')
    col9.write('_??tude de l\'influence d\'??l??ments d\'addition sur les propri??t??s de stockage de l\'hydrog??ne dans le syst??me Ti-V-Fe._')
    
    st.text('')        
    st.text('')
    st.text('')        
    st.text('') 
    col1,col2,col3=st.beta_columns(3)
    col2.image(publi_prix,use_column_width=True)#width=220)
    col2.write(pr)
    col2.write('1er prix : _Pr??sentation Th??se CEA_, organis?? au Liten')
    st.text('')        
    st.text('')  

### General:
def catego(option):

    if option =='Accueil':
        page_accueille()
        
    elif option == 'Comp??tences' :
        page_competence()    

    elif option == 'Formations' :
        page_formation()      

    elif option == 'Exp??riences' :
        page_experience()      

    elif option == 'Int??r??ts' :
        page_interet()  

    elif option == 'Publications' :
        page_publi()  

    elif option == 'M??dias' :
        page_media() 
    
### Display :
st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)    
st.sidebar.image(profil_img,width=220)
st.sidebar.title('Jean-Beno??t DENIS, Ph.D')
st.sidebar.subheader("Data Scientist - Ing??nieur")

st.sidebar.image(bar_img,use_column_width=True)
st.sidebar.markdown("<h1 style='text-align: center; color: blue;'>Navigation</h1>", unsafe_allow_html=True)
option = st.sidebar.selectbox('',['Accueil',
                                            'Comp??tences',
                                            'Formations',
                                            'Exp??riences',
                                            'Int??r??ts',
                                            'Publications',
                                            'M??dias'
                                            ]) 
st.sidebar.text('')
st.sidebar.text('')                                            
st.sidebar.image(bar_img,use_column_width=True)


#st.sidebar.write('31 ans - Permis B')
st.sidebar.write(':telephone_receiver: 06 29 07 69 72')
st.sidebar.write(':e-mail: [jeanbenoitdenis@gmail.com](mailto:jeanbenoitdenis@gmail.com)')
st.sidebar.write(':round_pushpin:[4 Rue Hector Blanchet 38500 Voiron](https://goo.gl/maps/E8iCnmAg6AetDBy76)')




st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: {2560}px;
        padding-top: {0}rem;
        padding-right: {5}rem;
        padding-left: {5}rem;
        padding-bottom: {0}rem;
    }}
    .reportview-container .main {{
        color: {'black'};
        background-color: {'white'};
    }}
</style>
""",
        unsafe_allow_html=True,
    )
 
catego(option)

####################################################################    

