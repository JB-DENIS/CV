# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 09:26:15 2021

@author: JB
"""

import streamlit as st 
import streamlit.components.v1 as components
from PIL import Image 

st.set_page_config(layout="centered")



### Chargement des images :
    
img_size=(150,150) 
   
profil_img=Image.open('img/profils2.png')

comp_duo=Image.open('img/comp_duo2.jpg')
comp_ico=Image.open('img/comp_ico.jpg')

form_road=Image.open('img/form_road2.jpg')

exp_data=Image.open('img/exp_data.jpg').resize(img_size)
exp_chimie=Image.open('img/exp_chimie.jpg').resize(img_size)
exp_open=Image.open('img/exp_open.jpg').resize(img_size)
exp_data_oc=Image.open('img/exp_data_oc.jpg').resize((240,200))
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

glob_comp=Image.open('img/glob_comp.jpg')
glob_int=Image.open('img/glob_int.jpg')
glob_exp=Image.open('img/glob_exp.jpg')
glob_form=Image.open('img/glob_form.jpg')
glob_kw2=Image.open('img/glob_kw3.jpg')

media_yt_f = open('video/YT.mp4', 'rb')
media_yt = media_yt_f.read()


### Pages

def page_accueille() :
    st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)    
    st.markdown("<h1 style='text-align: center;'>Bienvenue sur mon CV interactif</h1>", unsafe_allow_html=True)

    st.info(' Choisissez une catégorie dans le menu déroulant **_Navigation_** à gauche.')  
   
    col1, col2, col3  = st.beta_columns((2,0.2,2.8))
    col1.subheader('Compétences')
    col1.image(glob_comp,use_column_width=True)
    col3.subheader('Expériences')
    col3.image(glob_exp,use_column_width=True)
    
    col4, col5, col6, col7, col8 = st.beta_columns((3,0.00000001,1.1,0.2,1.4))
    col4.subheader('Intérets')
    col4.image(glob_int,use_column_width=True)
    col6.subheader('Formations')
    col6.image(glob_form,use_column_width=True)
    col8.subheader('Keywords')
    col8.image(glob_kw2,use_column_width=True)
     
   
                 
def page_competence  ():
    st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)
    st.header('Compétences')
    st.text('')
    st.text('')
    st.image(comp_duo,use_column_width=True)#width=600) 
    st.image(comp_ico,use_column_width=True)#width=600)  

   
def page_formation  (): 
    st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)
    st.header('Formations')
    st.text('')
    st.text('')
    st.image(form_road,use_column_width=True)#width=800)
    
    
def page_experience():
    st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)
    st.header('Expériences')
    st.text('')
    st.text('')
    st.markdown("<h5 style='text-align: center; color: gray;'>Choisissez une catégorie</h5>", unsafe_allow_html=True)
    st.text('')
    col1, col2, col3  = st.beta_columns(3)
    col1.image(exp_data,use_column_width=True)
    col2.image(exp_chimie,use_column_width=True)
    col3.image(exp_open,use_column_width=True)
    
    col4, col5, col6, col7, col8, col9  = st.beta_columns((0.5,1,0.35,1,0.45,1))
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
        col13.write('La volonté de partir en formation Data Scientist vient du constat, fait lors de mes diverses expériences professionnelles, que les datas ont investi tous les cœurs de métier. La pertinence et la puissance d’utiliser ces datas pour comprendre et prédire des comportements sont apparues comme une suite logique à mon parcours professionnel et ainsi acquérir un nouvel outil polyvalent.')
        col14.image(exp_data_oc,use_column_width=True)
        
        st.subheader('Missions')
        st.write('La formation se décline sous forme de 7 projets professionnels utilisant des données terrain. L’environnement mis en place pour ces projets est le language Python et la méthodologie de travail appliquée est la méthode S.M.A.R.T.')
        st.text('')
        st.write('Exemples de projets réalisés :')
        st.text('')
        col15, col16 = st.beta_columns((1,1))
        col15.write('**_Anticipation de la consommation et des émissions de bâtiments_** ')
        col15.write('Utiliser des données recueillies auprès d’immeubles de nouvelle génération afin de modéliser et prédire les consommations énergétiques et émissions de gaz à effet de serres en fonction du type de bâtiment.')
        col16.write('**_Segmentation des clients d\'un site d\'e-commerce _** ')
        col16.write('Réaliser un clustering d’utilisateurs d’un site d’e-commerce afin d’établir des actions commerciales ciblées.')
        
        st.text('')
        col17, col18 = st.beta_columns((1,1))
        col17.write('**_Classification automatique de biens de consommation_** ')
        col17.write('Mise en place d’un outil de classification automatique de produits de consommation en fonction de leurs descriptifs (texte) et de leurs photos (visuel).')
        col18.write('**_Implémentation d’une métrique métier pour le secteur bancaire_** ')
        col18.write('Construire une métrique métier pour la modélisation d’un score d’attribution de prêt bancaire, interprétation sur Dashboard et déploiement de l\'API.')
        
        st.subheader('Réalisations')
        st.write(':black_small_square: Data Mining, Etude statistique')
        st.write(':black_small_square: Pre-processing, feature engineering, réduction dimensionnelle (ACP)')
        st.write(':black_small_square: Machine learning supervisé : régression, kNN, SVM,  Random Forest, XGBoost, LightGBM')
        st.write(':black_small_square: Machine learning non supervisé : Kmeans, DBScan, HAC, GMM')
        st.write(':black_small_square: Métrique métier, optimisation bayésienne, stacking')
        st.write(':black_small_square: Deep Learning, NLP (BoW, Tf-IDF, Embedding), visuel (BoVW, CNN, Transfert learning)')
        st.write(':black_small_square: Spark, AWS')
        st.write(':black_small_square: Déploiement  API, Dashboard ')
        st.write(':black_small_square: Analyse de résultats, reporting et vulgarisation ')
        st.write(':black_small_square: GitHub rassemblant tous les projets (Voir **Média**) ')
        
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
        col10.header('Ingénieur de Recherche  Entrepreneur ')
        st.subheader('_Recyclage des moteurs d’éolienne_')
        col11.text('')
        col12.header('2017-2018')
        
        st.text('')
        col13, col14 = st.beta_columns((2.5,1))
        col13.subheader('Contexte')
        col13.write('La production d’énergie par l’éolien représentait 6.3% du parc français en 2019 et ne cesse d’augmenter. Cette diversification des moyens de production d’énergie pose de nouveaux enjeux notamment au niveau environnemental. En effet une seule éolienne comprend une grande quantité de Terres Rares, éléments critiques en fort épuisement et principalement produits en Chine. Cet enjeu a nourri la volonté de lancer le projet de création de la start-up RECUP’TR afin de développer un procédé propre et local de recyclage des Terres Rares contenues dans les aimants permanents d’éoliennes.')
        col14.image(exp_sc_broyeur,use_column_width=True)
        
        st.subheader('Missions')
                                                        
        st.text('')
        col15, col16 = st.beta_columns((1,1))
        col15.write('**_Développement et amélioration du procédé de production _** ')
        col16.write('**_Gestion de projets / Management d’équipe technique _** ')
        
        st.text('')
        col17, col18 = st.beta_columns((1,1))
        col17.write('**_Entrepreneuriat_** ')
        col18.write('**_Etude de marché et profils clients (Datas BPI France)_** ')
        
        st.subheader('Réalisations')
        st.write(':black_small_square: Synthèse par broyeur planétaire, presse, traitement thermique sous H2, Extraction chimique')
        st.write(':black_small_square: DRX, MEB, Granulométrie, Bobine Supra, ATG, EPMA')
        st.write(':black_small_square: Rédaction du mode opératoire de production (Enveloppe SOLEAU)')
        st.write(':black_small_square: Réalisation des procédures de manipulation et de sécurité')
        st.write(':black_small_square: Conception et mise en place d’outils techniques')
        st.write(':black_small_square: Rendement triplé en fin de mission')
        st.write(':black_small_square: Preuve de concept opérationnelle')
        
        ###
        st.text('')
        st.text('')
        st.text('')
        col10, col11, col12  = st.beta_columns((2,1,1))
        col10.header('Ingénieur doctorant ')
        st.subheader('_Optimisation du stockage d’énergie par hydrogène_')
        col11.text('')
        col12.header('2012-2016')
        
        st.text('')
        col13, col14 = st.beta_columns((2.5,1))
        col13.subheader('Contexte')
        col13.write('La production d’énergie est devenue un enjeu majeur de notre époque, et la monté des énergies renouvelables offre de nombreuses possibilités. Différentes thématiques de développement dans la chaîne de production s’ouvrent alors et notamment la problématique du stockage de cette énergie. Le vecteur énergétique hydrogène permet une alternative à l’électricité et exploite de nouvelles technologies avec un impact environnemental réduit. Cependant ces techniques sont encore jeunes et coûteuses. Dans cette optique, les travaux réalisés au cours de cette thèse se sont focalisés sur la diminution des coûts de production des matériaux de stockage de l’hydrogène et sur l’optimisation du procédé d\'élaboration. ')
        col14.image(exp_sc_four,use_column_width=True)
        
        st.subheader('Missions')
        st.text('')
        col15, col16 = st.beta_columns((1,1))
        col15.write('**_Métallurgie, caractérisations physico-chimique _** ')
        col16.write('**_Manipulation de Gaz en zone ATEX _** ')
        
        st.text('')
        col17, col18 = st.beta_columns((1,1))
        col17.write('**_Gestion de projets, réunions, plan d\'expérience, cahier des charges_** ')
        col18.write('**_Conception bancs essai et outils techniques, maintenance_** ')
        
        st.subheader('Réalisations')
        st.write(':black_small_square: Elaboration d’alliages en four à induction – Frittages. Métallurgie, Hydrure sous pression ')
        st.write(':black_small_square: DRX, MEB, EDX, EPMA, DSC, mesure PCT, cyclage')
        st.write(':black_small_square: Modélisation des lois de prédiction de volume de maille d\'un alliage quinaire')
        st.write(':black_small_square: Réalisation d\'un abaque PCT sur l\'utilisation d\'Al et Si dans un système TiVFe')
        st.write(':black_small_square: Procédure d\'élaboration optimisée')
        st.write(':black_small_square: Manuscrit de thèse - Rapport sur les Energies (Voir **Publications**)')
        st.write(':black_small_square: **1er Prix Présentation de thèse** (Voir **Publications**)')
        
        ###
        st.text('')
        st.text('')
        st.text('')
        col10, col11, col12  = st.beta_columns((2,1,1))
        col10.header('Ingénieur stagiaire  ')
        st.subheader('_Etude environnementale de particules ITER-Like_')
        col11.text('')
        col12.header('2012')
        
        st.text('')
        col13, col14 = st.beta_columns((2.5,1))
        col13.subheader('Contexte')
        col13.write('Le projet ITER sur la fusion thermonucléaire a pour objectif de produire une énergie propre et quasi illimitée. Cependant la technologie employée pose de nombreuses interrogations et notamment sur l’impact humain et environnemental des sous-produits de fusion générés lors de l’utilisation du réacteur.  Dans cette idée,  il a été décidé de recréer en laboratoire et d’étudier des nano-particules de tungstène dites «ITER-LIKE» afin d’analyser leurs toxicités.')
        col14.image(exp_sc_laser,use_column_width=True)
        
        st.subheader('Missions')
        st.text('')
        col15, col16 = st.beta_columns((1,1))
        col15.write('**_Mise en place et responsable banc d\'essai_** ')
        col16.write('**_Réalisation de nano-particules par ablation laser (ns / ps)_** ')
        
        st.text('')
        col17, col18 = st.beta_columns((1,1))
        col17.write('**_Caractérisation physico-chimique_** ')
        col18.write('**_Formation MEB_** ')
        
        st.subheader('Réalisations')
        st.write(':black_small_square: Production de nano-particules ITER-Like')
        st.write(':black_small_square: MEB, EDS, AFM, granulométrie')
        st.write(':black_small_square: Rapport pour le projet ITER')
        st.write(':black_small_square: Résultats envoyés pour étude toxicologique (suite du projet) ')
       
        ###
        st.text('')
        st.text('')
        st.text('')
        col10, col11, col12  = st.beta_columns((2,1,1))
        col10.header('Ingénieur stagiaire  ')
        st.subheader('_Création de nouvel accumulateur électrique_')
        col11.text('')
        col12.header('2011')
        
        st.text('')
        col13, col14 = st.beta_columns((2.5,1))
        col13.subheader('Contexte')
        col13.write('Le Projet ROPAS visait la production de batteries flexibles imprimées sur papier. Afin de s’affranchir des constituants classiques et coûteux d’un accumulateur et répondre à l’appauvrissement du lithium, le projet avait pour objectif la réalisation de nouveaux matériaux d’électrodes organiques (ORB) pour accumulateur fonctionnant aussi bien au Lithium, qu’au Sodium.')
        col14.image(exp_sc_bat,use_column_width=True)
        
        st.subheader('Missions')
        st.text('')
        col15, col16 = st.beta_columns((1,1))
        col15.write('**_Synthèse organique et polymérisation sous atmosphère inerte_** ')
        col16.write('**_Mise en place et optimisation banc d\'essai_** ')
        
        st.text('')
        col17, col18 = st.beta_columns((1,1))
        col17.write('**_Caractérisation physico-chimique_** ')
        col18.write('**_Formulation et mise en œuvre d’encre_** ')
        
        st.subheader('Réalisations')
        st.write(':black_small_square: Synthèse organique et polymérisation sous atmosphère inerte (Boîte à gants)')
        st.write(':black_small_square: Formulation et mise en œuvre d’encre')
        st.write(':black_small_square: RMN, IR,ATD, ATG, Voltampérométrie, Cyclage d’accumulateur')
        st.write(':black_small_square: Synthèse d\'un nouveau matériau ORB')
        st.write(':black_small_square: **Dépôt de brevet** (Voir **Publications**)')
        st.write(':black_small_square: **Récompensé Prime stagiaire CEA** ')
        
        ###
        st.text('')
        st.text('')
        st.text('')
        col10, col11, col12  = st.beta_columns((2,1,1))
        col10.header('Technicien stagiaire  ')
        st.subheader('_Expérience professionnelle à Singapour_')
        col11.text('')
        col12.header('2010')
        
        st.text('')
        col13, col14 = st.beta_columns((2.5,1))
        col13.subheader('Contexte')
        col13.write('Dans une volonté d’ouverture à l’internationale, cette expérience professionnelle s’est tenue à Singapour à un poste de technicien sur chaîne de production d\'enzyme pour le textile.')
        col14.image(exp_sc_enz,width=70)
        
        st.subheader('Missions')
        st.text('')
        col15, col16 = st.beta_columns((1,1))
        col15.write('**_Essais techniques sur banc d\'essai_** ')
        col16.write('**_Contrôle qualité produits_** ')
        
        st.text('')
        col17, col18 = st.beta_columns((1,1))
        col17.write('**_Lancement de machine de production_** ')
        col18.write('')
        
        st.subheader('Réalisations')
        st.write(':black_small_square: Reporting, contrôle qualité')
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
        col10.header('Projet césure - Artisanat  ')
        st.subheader('_Rénovation d’une maison de A à Z_')
        col11.text('')
        col12.header('2019-2020')
        
        st.text('')
        col13, col14 = st.beta_columns((2.5,1))
        col13.subheader('Contexte')
        col13.write('Achat d\'une maison à rénover.')
        col14.image(exp_diver_maison,use_column_width=True)
                       
        st.subheader('Réalisations')
        st.write(':black_small_square: Réalisation des gros œuvres sur chantier') 
        st.write(':black_small_square: Création d’espaces de vie') 
        st.write(':black_small_square: Mise à niveau électrique – circuit de plomberie') 
        st.write(':black_small_square: Ebénisterie') 
        st.write(':black_small_square: Lancement chaîne YouTube sur le travail du bois (Voir **Média**)') 
        
        ###
        st.text('')
        st.text('')
        st.text('')
        col10, col11, col12  = st.beta_columns((2,1,1))
        col10.header('Opérateur, cuisinier, fermier')
        st.subheader('_Woofing au Japon_')
        col11.text('')
        col12.header('2008')
        
        st.text('')
        col13, col14 = st.beta_columns((2.5,1))
        col13.subheader('Contexte')
        col13.write('Opportunité de découvrir le Japon tout en travaillant dans un centre d\'activités.')
        col14.image(exp_diver_jap,use_column_width=True)
        
        st.subheader('Missions')
        st.text('')
        col15, col16 = st.beta_columns((1,1))
        col15.write('**_Responsable stand "Pizza" et stand "Grillade"_** ')
        col16.write('**_Atelier de menuiserie_** ')
        
        st.text('')
        col17, col18 = st.beta_columns((1,1))
        col17.write('**_Accompagnement équitation_** ')
        col18.write('**_Travaux de la ferme_**')
        
        st.subheader('Réalisations')
        st.write(':black_small_square: Echange culturel et linguistique')
        
        ###
        st.text('')
        st.text('')
        st.text('')
        col10, col11, col12  = st.beta_columns((2,1,1))
        col10.header('Opérateur')
        st.subheader('_Vacancier - Intérimaire_')
        col11.text('')
        col12.header('2007-2009')
        
        st.text('')
        col13, col14 = st.beta_columns((2.5,1))
        col13.subheader('Contexte')
        col13.write('Chaîne de production d’emballage carton.')
        col14.image(exp_diver_cart,width=120)
        
        st.subheader('Missions')
        st.text('')
        col15, col16 = st.beta_columns((1,1))
        col15.write('**_Réglage machine de production_** ')
        col16.write('**_Mise en palette sortie chaîne de production_** ')
        
        st.text('')
        col17, col18 = st.beta_columns((1,1))
        col17.write('**_Contrôle qualité_** ')
        col18.write('')
        
        st.subheader('Réalisations')
        st.write(':black_small_square: Contrôle qualité')
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
    st.header('Intérets')
    st.text('')
    st.text('')
    st.image(interet_mot,width=800)#use_column_width=True)
    
      
def page_media():
    st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)
    st.header('Médias')
    st.text('')
    
    cv=('[**CV**](https://drive.google.com/file/d/1m6RCFIE46yZG5iUjaUsNpnvu5DaDBths/view?usp=sharing)')
    lm=('[**Lettre de motivation**](https://drive.google.com/file/d/1hpbAiw7URmtNtQo_BdIHHOX12_Zpb3GC/view?usp=sharing)')
    lr=('[**Lettre de recommandation**](https://drive.google.com/file/d/1UoU_yFMkkjtdxRiluyNAN9NfIWck2mOk/view?usp=sharing)')
    git=('[**GitHub**](https://github.com/JB-DENIS)')
    lin=('[**LinkedIn**](https://linkedin.com/in/jean-benoît-denis-38000)')
    yt=('[**YouTube**](https://www.youtube.com/channel/UC1i8IXzTvu7rhaXBCLMaDmQ)')
    
    st.markdown("<h5 style='text-align: center; color: gray;'>Cliquez sur un média pour accéder au contenu</h5>", unsafe_allow_html=True)
    st.text('')
    st.text('')
    
    col4, col5, col6, col7, col8, col9, col10 = st.beta_columns((0.3,1,0.05,1,0.3,1,0.04))
    col5.image(media_cv,width=125)
    col7.image(media_lm,width=125)
    col9.image(media_lr,width=125)
        
    col4, col5, col6, col7, col8, col9, col10 = st.beta_columns((0.59,1,0.05,1,0.3,1,0.04))
    col5.markdown(cv, unsafe_allow_html=True)
    col7.markdown(lm, unsafe_allow_html=True)
    col9.markdown(lr, unsafe_allow_html=True)    
    
    st.text('')        
    st.text('')        
        
    col4, col5, col6, col7, col8= st.beta_columns((0.8,1,0.2,1,0.6))
    col5.image(media_git,width=125)
    col7.image(media_linkedin,width=125)
          
    col4, col5, col6, col7, col8= st.beta_columns((1.3,1,0.5,1,0.8))
    col5.markdown(git, unsafe_allow_html=True)
    col7.markdown(lin, unsafe_allow_html=True)
    
    st.text('')        
    st.text('')
    
    st.video(media_yt)
    col1, col2, col3  = st.beta_columns((4,1,4))
    col2.markdown(yt, unsafe_allow_html=True)  

            
def page_publi():
    st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)
    st.header('Publications')
    st.text('')
    br=('[**Brevet**](https://drive.google.com/file/d/1RZVpIPAJiq4zO9LPjO2_ahqiKJrSqQ2A/view?usp=sharing)')
    po=('[**Poster**](https://drive.google.com/file/d/1btDY31nkJ-ycOGMaT_ar9SBzTMzDSllW/view?usp=sharing)')
    th=('[**Thèse**](https://drive.google.com/file/d/1-OMgCIu-agnUHLJW8uUhvnJHNP_fdg7t/view?usp=sharing)')
    pr=('[**Présentation Thèse**](https://drive.google.com/file/d/143D5-Euw0HwPIUcxHw49HVQ_j2J1KKZM/view?usp=sharing)')
        
    st.markdown("<h5 style='text-align: center; color: gray;'>Cliquez sur un lien pour accéder au contenu</h5>", unsafe_allow_html=True)
    st.text('')
    st.text('')
    
    col4, col5, col6, col7 = st.beta_columns(4)
    col4.image(publi_brevet,use_column_width=True)
    col5.image(publi_poster,use_column_width=True)
    col6.image(publi_these,use_column_width=True)
    col7.image(publi_prix,width=220)
        
    col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.beta_columns((0.6,1,0.9,1,0.9,1,0.9,1,0.0001))
    col5.markdown(br, unsafe_allow_html=True)
    col7.markdown(po, unsafe_allow_html=True)
    col9.markdown(th, unsafe_allow_html=True) 
    col11.markdown(pr, unsafe_allow_html=True)
    
    st.text('')        
    st.text('')  

### General:
def catego(option):

    if option =='Accueil':
        page_accueille()
        
    elif option == 'Compétences' :
        page_competence()    

    elif option == 'Formations' :
        page_formation()      

    elif option == 'Expériences' :
        page_experience()      

    elif option == 'Intérets' :
        page_interet()  

    elif option == 'Publications' :
        page_publi()  

    elif option == 'Médias' :
        page_media() 
    
### Display :
st.markdown("""<a id="top"></a>""",unsafe_allow_html=True)    
st.sidebar.image(profil_img,width=220)
st.sidebar.title('Jean-Benoît DENIS')
st.sidebar.subheader("Ingénieur Data Scientist")
st.sidebar.write('31 ans - Permis B')
st.sidebar.write(':round_pushpin:[4 Rue Hector Blanchet 38500 Voiron](https://goo.gl/maps/E8iCnmAg6AetDBy76)')
st.sidebar.write(':telephone_receiver: 06 29 07 69 72')
st.sidebar.write(':e-mail: [jeanbenoitdenis@gmail.com](mailto:jeanbenoitdenis@gmail.com)')

option = st.sidebar.selectbox('Navigation',['Accueil',
                                            'Compétences',
                                            'Formations',
                                            'Expériences',
                                            'Intérets',
                                            'Publications',
                                            'Médias'
                                            ])      

    
catego(option)   

####################################################################    

