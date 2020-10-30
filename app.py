import streamlit as st
import numpy as np
import seaborn as sns
import pandas as pd 
from PIL import Image
import matplotlib.pyplot as plt
from sklearn import preprocessing
st.set_option('deprecation.showPyplotGlobalUse', False)
def main():
    activities=['About','Initital Period Analysis(January-March)','April Month Analysis','May Month Analysis','Conclusion','Developer']
    option=st.sidebar.selectbox('Menu Bar:',activities)
    if option=='About':
        html_temp = """
        <div style = "background-color: RED; padding: 10px;">
            <center><h1>ABOUT PROJECT</h1></center>
        </div><br>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        st.header('What is Corona Virus?')
        image=Image.open('1.png')
        st.image(image,use_column_width=True)
        st.write('Coronaviruses are a large family of viruses which may cause illness in animals or humans. In humans, several coronaviruses are known to cause respiratory infections ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS). The most recently discovered coronavirus causes coronavirus disease COVID-19. The virus that causes COVID-19 is mainly transmitted through droplets generated when an infected person coughs, sneezes, or exhales. These droplets are too heavy to hang in the air, and quickly fall on floors or surfaces. You can be infected by breathing in the virus if you are within close proximity of someone who has COVID-19, or by touching a contaminated surface and then your eyes, nose or mouth.')
        st.header('COVID-19 INDIA LATEST NEWS!!')
        st.write('Coronavirus India Live Updates —Total Coronavirus cases in India has crossed the 4,73,000-mark while COVID 19 death toll is near 14,894 in the country. As per the data shared by the Ministry of Health and Family Welfare, the total number of COVID-19 cases in India now are 4,88,968 , with 2,16,968 active cases and 2,72,000 cured/discharged patients. As many as 15,359 people have died. The recovery rate in the country stands at 57.43 per cent, Health Ministry official said. The Global hunt for coronavirus COVID 19 vaccine is on even as large parts of the world is battling a war against the highly contagious disease. Total confirmed coronavirus cases around the world are 9.44 M. So far, 4,87,210 people have died due to COVID 19, according to Johns Hopkins University Coronavirus Resource Center data.')
        st.header('ABOUT THE DATA SET')
        st.write('This project gives a detailed analysis about the Covid -19 pandemic in India during the period between January and May. For this , we will be using multiple datasets from various sources . We will be using datasets like age_group_details , hospital_beds_in_India , Individual_details , per_day_cases , covid-19_in_India etc.')   
    elif option=='Initital Period Analysis(January-March)':
        st.title("Initital Period Analysis(January-March)")
        fread=pd.read_csv("AgeGroupDetails.csv")
        fread1=fread.select_dtypes(include=['float64','int64'])
        fread2=fread.select_dtypes(include=['object'])

        st.header('Details about the percentage of the age group being affected in India')
        st.write(fread2.head())
        st.write('The dataframe here gives us the details about the different age groups and the percentage of affected people in that group.')

        le=preprocessing.LabelEncoder()
        labels=le.fit_transform(fread['AgeGroup'])

        st.header('Graph portraying the current cases and the age groups affected in India')
        sns.set(rc={'figure.figsize':(11,8)})
        x=fread.AgeGroup
        y=fread.TotalCases
        y_pos=np.arange(len(x))
        plt.xticks(y_pos,x)
        plt.xticks(rotation=90)
        plt.xlabel('Age Groups')
        sns.kdeplot(y_pos,y,cmaps='Reds',shade=True,cbar=True)
        st.pyplot()
        st.write('From the above graph we can clearly see that the older age group is at more risk of getting affected by the coronavirus. The maximum number of cases are found in the age group of 50–59 and 60–69.')
        st.write('To represent the above graph we have used a kdeplot from the seaborn library of python.')

        st.header('Total number of cases,deaths,cured patients in India')
        covid=pd.read_csv("covid_19_india.csv")
        sns.pairplot(covid, palette="Set2")
        st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.write('These are the graphs showing the Ratio of Deaths that have taken place in the three months to the number of patients who have recovered and the information related to it . This is a pairplot which was made using the seaborn library of python.')
        
        st.header('Number of People Cured vs Deaths')
        plt.figure(figsize=(5,5))
        cured=covid[covid['Cured']==True]
        deaths=covid[covid['Deaths']==True]
        slices_hours = [cured['Time'].count(),deaths['Time'].count()]
        activities = ['Cured', 'Deaths']
        colors = ['aqua', 'orange']
        explode=(0,0.1)
        plt.pie(slices_hours, labels=activities,explode=explode, colors=colors, startangle=90, autopct='%1.1f%%',shadow=True)
        plt.show()
        st.pyplot()
        st.write('From this pie chart we can see that death rates were around 60.2% while the cured rates were around 39.8% . So, it can be concluded that during the initital stage of this pandemic the recovery rates we low , below 50% .')

        st.header('Symptoms observed in hospitalized patients with COVID-19')
        st.write('Below we list the symptoms, with percentages representing the proportion of patients displaying that symptom, as observed in hospitalized patients tested and identified as having laboratory-confirmed COVID-19 infection. These findings refer to hospitalized patients, therefore generally representing serious or critical cases. The majority of cases of COVID-19 (about 80%) is mild.')
        st.write('The most common symptoms of COVID-19 are fever, tiredness, and dry cough. Some patients may have aches and pains, nasal congestion, runny nose, sore throat or diarrhea. These symptoms are usually mild and begin gradually. Some people become infected but don’t develop any symptoms and don’t feel unwell. Most people (about 80%) recover from the disease without needing special treatment. Around 1 out of every 6 people who gets COVID-19 becomes seriously ill and develops difficulty breathing. Older people, and those with underlying medical problems like high blood pressure, heart problems or diabetes, are more likely to develop serious illness. People with fever, cough and difficulty breathing should seek medical attention.')
        symptoms={'symptoms':['Fever','Tiredness','Dry-cough','Shortness of breath','aches and pains','Sore throat','Diarrhoea','Nausea','vomiting','abdominal pain'],'percentage':[98.6,69.9,82,16.6,14.8,13.9,10.1,10.1,3.6,2.2]}
        symptoms=pd.DataFrame(data=symptoms,index=range(10))
        st.write(symptoms)
        st.write('The above table shows us the information regarding the different symptoms observed on patients around the world and the percentage of patients having these symptoms while being affected from Covid-19.')

        plt.figure(figsize=(10,5))
        height=symptoms.percentage
        bars=symptoms.symptoms
        y_pos=np.arange(len(bars))
        my_colors=['violet','indigo','blue','green','yellow','orange','red']
        plt.bar(y_pos,height,color=my_colors)
        plt.xticks(y_pos,bars)
        plt.xticks(rotation=90)
        plt.xlabel("Symptoms",size=30)
        plt.ylabel("Percentage",size=30)
        plt.title("Symptoms of COVID-19",size=45)
        plt.show()
        st.pyplot()
        st.write('This bar graph maps the various symptoms according to the percentage of people having these symptoms . On observing this graph carefully we can see that fever and dry-cough were the most common symptoms found in patients . This doesn’t mean that if you are having the other symptoms you are less prone to have coronavirus . Having any of these symptoms means that you should take care of yourself while self quarantining yourself and getting a covid-19 test.')


        plt.figure(figsize=(10,10))
        plt.title("Symptoms of COVID-19",size=20)
        plt.pie(symptoms['percentage'],colors=['violet','indigo','blue','green','yellow','orange','red'],autopct="%1.1f%%")
        plt.legend(symptoms['symptoms'],loc='best')
        plt.show()
        st.pyplot()
        st.write('This pie chart also gives the same information as above .')

        st.header('Details of Hospitals and healthcare facilities in India')
        hosp=pd.read_csv("HospitalBedsIndia.csv")
        hosp1=hosp.select_dtypes(include=['float64','int64'])
        hosp2=hosp.select_dtypes(include=['object'])

        
        health=hosp.drop([36])
        obj=list(health.columns[2:8])

        for ob in obj:
            health[ob]=health[ob].astype(int,errors='ignore')

        
        plt.suptitle('HEALTH FACILITIES STATEWISE',fontsize=20)
        fig = plt.figure(figsize=(20,10)) 
        plt1 = fig.add_subplot(221) 
        plt2 = fig.add_subplot(222) 
        plt3 = fig.add_subplot(223) 
        plt4 = fig.add_subplot(224) 

        primary=health.nlargest(12,'NumPrimaryHealthCenters_HMIS')

        plt1.set_title('Primary Health Centers')
        plt1.barh(primary['State/UT'],primary['NumPrimaryHealthCenters_HMIS'],color ='gold');

        community=health.nlargest(12,'NumCommunityHealthCenters_HMIS')
        plt2.set_title('Community Health Centers')
        plt2.barh(community['State/UT'],community['NumCommunityHealthCenters_HMIS'],color='coral')

        dist=health.nlargest(12,'NumDistrictHospitals_HMIS')
        plt3.set_title("District Hospitals")
        plt3.barh(dist['State/UT'],dist['NumDistrictHospitals_HMIS'],color='lightskyblue')

        subd=health.nlargest(12,'TotalPublicHealthFacilities_HMIS')
        plt4.set_title('PUblic Health Facilities')
        plt4.barh(subd['State/UT'],subd['TotalPublicHealthFacilities_HMIS'],color='violet')

        fig.subplots_adjust(hspace=.5,wspace=0.2)
        st.pyplot()
        st.write('First of all , here we have imported the dataset called the HospitalbedsinIndia . Here we can see various subplots giving the details about the numbers of beds across various states of India . The four graphs gives the information of beds in primary heath centers , community health centers , district hospitals and public health facilities.')
        

        indiv=pd.read_csv("IndividualDetails.csv")
        indiv2=indiv.select_dtypes(include=['float64','int64'])
        indiv3=indiv.select_dtypes(include=['object'])

        st.header('Percentage of Males and Females affected')
        plt.figure(figsize=(5,10))
        male=indiv[indiv['gender']=='M']
        female=indiv[indiv['gender']=='F']
        slices_hours=[male['age'].count(),female['age'].count()]
        activities=['Male','Female']
        colors=['gold','silver']
        explode=(0,0.1)
        plt.pie(slices_hours,labels=activities,explode=explode,colors=colors,startangle=180,autopct="%1.1f%%",shadow=True)
        plt.show()
        st.pyplot()
        st.write('Here we have first imported the Individualdetails dataset form kaggle . Then we have plotted a pie chart showing the number of males and females affected from this virus. On observing this pie chart we can see that around 69% of males and around 31% females are affected from this virus. From this we can conclude that males are somewhat more exposed to this virus than females .')
        

    elif option=='April Month Analysis':
        st.title('APRIL Month Analysis of COVID-19')
        st.write('Till now we have seen a detailed analysis about the pandemic from the period between January and March . From now on we will be analyzing the situation till April 30th. For this analysis we have imported the dataset having information till the 30th of APRIL.')
        
        april=pd.read_csv("30-04-2020.csv")
        april2=april.select_dtypes(include=['float64','int'])
        april3=april.select_dtypes(include=['object'])

        le=preprocessing.LabelEncoder()
        labels=le.fit_transform(april['Death'])

        st.header('Death Value Counts')
        april.Death.value_counts().plot.bar(color=['gold','coral','aqua','skyblue','violet','pink'])
        st.pyplot()

        st.header('CURED,TOTAL CASES AND DEATHS')
        cases=april['Total Confirmed cases (Including 111 foreign Nationals)'].sum()
        cdm=april['Cured/Discharged/Migrated'].sum()
        d=april['Death'].sum()

        plt.figure(figsize=(5,5))
        plt.title("Current situation in india(April)",fontsize=20)
        labels='Total Cases','Cured','Death'
        sizes=[cases,cdm,d]
        explode=[0.1,0.1,0.1]
        colors=['gold','yellowgreen','aqua']
        plt.pie(sizes,labels=labels,colors=colors,explode=explode,autopct='%1.1f%%',shadow=True,startangle=90)
        plt.show()
        st.pyplot()
        st.write('This pie chart shows the percentage of remaining positive cases , the patients cured and the deaths across India till 30th of April , 2020. We can see that around 18.4% of total cases observed has cured till now . While the death percentage is around 2.1% which has decreased from the previous few months . This means the number of people getting cured has increased and this seems to be a good sign. A lot of population still seem to be positive from this virus till now.')

        
        april['active']=april['Total Confirmed cases (Including 111 foreign Nationals)']-april['Death']-april['Cured/Discharged/Migrated']
        st.subheader('Total active cases:')
        st.write(april['active'].sum())
        st.subheader('Total Confirmed cases (Including 111 foreign Nationals:)')
        st.write(april['Total Confirmed cases (Including 111 foreign Nationals)'].sum())

        st.header('State wise Deaths')
        plt.figure(figsize=(9,10))
        height=april['Death']
        bars=april['Name of State / UT']
        y_pos=np.arange(len(bars))
        plt.barh(y_pos,height,color=['pink','skyblue','red','violet','green'])
        plt.yticks(y_pos,bars)
        plt.title("Death in states",size=30)
        plt.ylabel("States",size=20)
        plt.xlabel("Death",size=20)
        plt.show()
        st.pyplot()
        st.write('This bar graph gives the state wise deaths across different states of India. On close observation , we can note that the maximum deaths are from Maharashtra(400+ ) followed by Gujarat(200+)and Madhya Pradesh. While the northeastern states have the least number of deaths .')


        st.header('STATE-WISE CURED/MIGRATED/DISCHARGED')
        plt.figure(figsize=(9,10))
        height=april['Cured/Discharged/Migrated']
        bars=april['Name of State / UT']
        y_pos=np.arange(len(bars))
        plt.barh(y_pos,height,color=['pink','skyblue','red','violet','green'])
        plt.yticks(y_pos,bars)
        plt.title("Cured/Discharged/Migrated in states",size=30)
        plt.ylabel("States",size=20)
        plt.xlabel("Cured",size=20)
        plt.show()
        st.pyplot()
        st.write('The bar graph here shows the number of patients cured across various states. The maximum number of people getting cured is in Maharashtra followed by Tamil Nadu , Delhi and Rajasthan.')


        st.header('State wise Mortality Rate')
        april['mortality']=april['Death']/april['active']*100
        plt.figure(figsize=(9,10))
        height=april['mortality']
        bars=april['Name of State / UT']
        y_pos=np.arange(len(bars))
        plt.barh(y_pos,height,color=['pink','skyblue','red','violet','green'])
        plt.yticks(y_pos,bars)
        plt.title("Mortality according to states",size=30)
        plt.ylabel("States",size=20)
        plt.xlabel("Mortality Rates",size=20)
        plt.show()
        st.pyplot()
        st.write('Mortality rate is a weighted average of the age-specific mortality rates per 100 000 persons, where the weights are the proportions of persons in the corresponding age groups of the WHO standard population.Mortality data allow health authorities to evaluate how they prioritize public health programs.')
        st.write('This bar graph gives the information about the mortality rate across various states of India . It can be seen observed from the graph that Meghalaya and Himachal Pradesh have equally highest mortality rate as compared to others. Odisha and Bihar seems to have the least mortality rate.')



        st.header('State wise active cases')
        plt.figure(figsize=(9,10))
        height=april['active']
        bars=april['Name of State / UT']
        y_pos=np.arange(len(bars))
        plt.barh(y_pos,height,color=['pink','skyblue','red','violet','green'])
        plt.yticks(y_pos,bars)
        plt.title("Active cases in states",size=30)
        plt.ylabel("States",size=20)
        plt.xlabel("Active",size=20)
        plt.show()
        st.pyplot()
        st.write('This bar graph gives us the information about the number of active cases in various states of India . We can notice that Maharashtra has the highest number of active cases which is still increasing at an alarming rate. Madhya Pradesh and Gujarat also have a high number of active cases . While there’s some relief in the northeastern states of India.')

        st.header('Perday New Cases')
        perday=pd.read_excel("per_day_cases.xlsx")
        perday2=perday.select_dtypes(include=['int64','float64','object'])
        st.write('Now we have imported the perdaycases dataset which gives us the infomation about the total cases and new cases of each day from January 1 to April 30.')


        st.header('APPALLING INCREASE in the COVID19 CASES PERDAY')
        plt.figure(figsize=(20,10),facecolor=(1,1,1))
        height=perday['New Cases']
        bars=perday['Date']
        y_pos=np.arange(len(bars))
        plt.plot(y_pos,height,'b-o',color='red')
        plt.plot(y_pos,height,'r--',color='white',linewidth=4)
        plt.xticks(y_pos,bars)
        plt.xticks(rotation=90)
        plt.title('New Daily Cases',size=40)
        plt.ylabel('Cases per Day',size=30)
        plt.xlabel('Date',size=30)
        ax = plt.axes()
        ax.set_facecolor("black")
        ax.grid(False)
        st.pyplot()
        st.write('This is a very important graph to analyse the situation . On closely observing the graph we can make a note that till 30th of March there was a very slight increase in the number of new cases everyday . But of after March , from the starting to April , the number of new cases began to increasing on an alarming rate which reached its peak value at the end of April by crossing more than 2500 new cases per day. One of the reason for this could be the more number of tests being done by the health authority across all over India.')


        st.header('IMPACT ON LIFESTYLE')
        st.write('This pandemic has affected our lifestyle in one way or the other . We are unable to lead our lives normally like we earlier used to do . We are now forced to lock ourselves in our home to quarantine ourselves . The GDP of the country is decreasing , we have no work to do , no schools , no college ,etc .')
        st.write('I have collected some of information about different lifestyles people are having now and percentage of people dealing with it.')
        lifestyle={'lifestyle':['Not waste food','Be environment conscious','Be more mindful of Health','Become more hygienic','More Family Time','Spend less on Clothes','Made in India products','Take work more seriously','Boycott Chinese goods'],'percentage':[67.7,45.6,44.3,40.5,31.8,31.4,26.4,25.5,24.6]}
        lifestyle=pd.DataFrame(data=lifestyle,index=range(9))
        st.write(lifestyle)
        st.write('To analyse this data in a more interactive way , let’s make a pie chart of this using python.')

        plt.figure(figsize=(10,10))
        plt.title("Impact on lifestyle of Indians",fontsize=20)
        plt.pie(lifestyle["percentage"],colors=['red','blue','green','pink','yellow','violet','silver','gold','skyblue'],autopct="%1.1f%%",shadow=True)
        plt.legend(lifestyle['lifestyle'],loc='upper right')
        plt.show()
        st.pyplot()
        st.write('From the pie chart , we can we that more number of people are in the favour of not wasting which is a very good gesture shown by most of people . While some people are more environment conscious and more mindful of health. Some people also believe that using Indian made domestic products can also help . I personally appreciate the use of made in India products as they can really help to prevent the fall of GDP in India.')
        st.write('After this , we are going to import another dataset named complete_covid which gives us the information about the total number of confirmed cases, deaths , cured along with longitude and latitude of the place of the patient and the state from which they belong. This dataset is available on the kaggle website.')
        app=pd.read_csv("complete.csv")
        
        st.header('Heatmap giving information about deaths across various states')
        heatmap1_data=pd.pivot_table(app,values='Death',index='Name of State / UT',columns='Date')
        sns.heatmap(heatmap1_data,cmap="RdYlGn",linewidths=0.01)
        st.pyplot()
        st.header('Heatmap giving information about Total confirmed cases across various states')
        h=pd.pivot_table(app,values='Total Confirmed cases',index=['Name of State / UT'],columns='Date')
        sns.heatmap(h,cmap=['skyblue','red','gold','green'],linewidths=0.05)
        st.pyplot()
        st.write('From this heatmap, we can observe that the cases are increases at an alarming rate in India,Maharashtra has the maximum number of covid-19 positives followed by Delhi and Tamil Nadu.')



    elif option=='May Month Analysis':
        st.title('Covid -19 ANALYSIS TILL MAY 28 , 2020')
        may=pd.read_csv("28-05-2020.csv")
        may=may.drop([33,34,35,36,37])
        st.write('Till now we have analysed the initital stage of this pandemic and the scenario in April in detail . Now let’s analyse for the month of May . For this let’s import the dataset which has information till May 28th ')
        st.subheader('Total confirmed cases till now:')
        cases=may['Total Confirmed cases*'].sum()
        st.write(cases)
        st.write('We can see that the number of confirmed cases till May 28 , are around 1,42,818. It’s getting to the end of the month of May and still the rate of patients getting affected from this virus is increasing day by day')
        
        df=may.nlargest(5,'Total Confirmed cases*')
        sns.barplot(x=df["Name of State / UT"],y=df["Total Confirmed cases*"],palette="Reds")
        plt.title("TOP 5 STATES WITH MAXIMUM CASES",size=30)
        st.pyplot()
        st.write('We can conclude from the above bar graph that the Total number of confirmed cases has crossed 50000 in Maharashtra , which is very shocking as well a reason to worry about . Here we can see the top 5 states having the highest number of confirmed cases.')


        
        sns.barplot(x=df["Name of State / UT"],y=df["Cured/Discharged/Migrated"],palette="Blues")
        plt.title("TOP 5 Infected STATES and the number of people cured",size=30)
        st.pyplot()
        st.write('Here we can note that a lot of people are recovering from this disease . Maharashtra being the fastest one to have that number of recoveries . It is good to see that the number of patients getting cured is increased in each and very states across India. Here we can see the number of patients cured in the top 5 states of India.')

        sns.barplot( x=df["Name of State / UT"], y=df["Deaths**"], palette="Reds")
        plt.title("TOP 5 Infected STATES and the number of Deaths",size=25)
        st.pyplot()
        st.write('Here we can see the top 5 states having the maximum number of deaths . On observing we can see that Maharashtra has the maximum number of death crossing the 1500 mark , followed by Gujarat and Rajasthan . The death rates are quite high in May as compared to the previous months . But it’s relief to see that the rate of recovery is also increasing .')
        
        sns.pairplot(may, kind="scatter")
        st.pyplot()

    
    elif option=='Conclusion':
        html_temp = """
        <div style = "background-color: Yellow; padding: 10px;">
            <center><h1>Conclusion</h1></center>
        </div><br>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        image=Image.open('2.png')
        st.image(image,use_column_width=True)
        st.header('Surfaces don’t seem to matter as much as originally thought')
        st.write('The surface or fomite theory — that you’ll get infected by coming into contact with objects that carry the virus, called fomites, like door handles, shopping carts, or packages — was the original leading contender because that’s how scientists and epidemiologists think most respiratory diseases are spread. For example, when a person sick with a cold coughs or sneezes, tiny snot and saliva particles that carry the virus go shooting out of their nose and mouth and land on nearby surfaces. If someone else touches that surface and then touches their mouth, nose, or eyes they could become infected with the virus. This is why we’re supposed to wash our hands before eating or preparing food, and after using public transportation, or touching door handles, especially during cold and flu season.')
        st.subheader('“I’m not saying that you can’t get it, that it’s impossible to get it from surfaces, but a very specific set of events have to occur for that to happen.”')
        st.write('Supporting this idea, an early study published in the New England Journal of Medicine found that SARS-CoV-2 survived on various surfaces for several days, including 24 hours on cardboard and 72 hours on plastic. Public health organizations recommended hand hygiene as the first line of defense against the virus, and there were runs on Lysol wipes and hand sanitizer at supermarkets and drugstores, the supply chains for which still have not recovered.')
        st.write('It turns out that despite the catastrophic harm it’s caused, the novel coronavirus is actually quite fragile, and it doesn’t like being out in the open where it can dry up. According to the NEJM paper, the virus’s half-life is a relatively short six hours, meaning that every six hours 50% of the virus shrivels up and becomes inactive or noninfectious. That means if you start with 100 virus particles, after six hours that number halves to 50 particles; six hours later there are 25 virus particles left, and fewer than 10 virus particles remain after 24 hours. However, if there are huge quantities of virus to start, many more will be left behind after each six-hour window, and it will take longer for all of the virus to disintegrate.')
        st.subheader('Instead of buying another can of Lysol, maybe invest in an air purifier, more comfortable two-ply cloth masks, or even an outdoor fire pit or space heater.')
        st.write('Regardless, it’s critical that people keep washing their hands — although that’s something we should all be doing for normal hygiene anyway — but, Goldman says, you don’t have to do anything excessive, like disinfecting your groceries.')
        st.header('Close range droplets are the new leading theory')
        st.write('In May, the CDC updated its guidelines to state that fomites were not a major source of transmission. Instead, the agency said, the primary route of infection was probably virus-laden droplets — those snot and saliva particles that are at the root of the fomite theory. But instead of worrying about them after they land on surfaces, the bigger concern now is coming into contact with the droplets while they’re still in the air.')
        st.write('When you expel air — whether it’s by sneezing, coughing, talking, singing, shouting, or even breathing — tiny bits of saliva, ranging in size from an imperceptible mist to visible spittle, are pushed out. Heavier particles fall to the ground relatively quickly and are categorized as droplets, while the tinier particles stay afloat in the air for longer. When talking and breathing, the typical droplet trajectory is about three to six feet, hence the six-foot distancing recommendation. If the droplets are expelled with more force, like with a sneeze or a cough, they can travel further before hitting the earth.')
        st.write('Being in close contact with someone raises the risk that you’ll be exposed to the small droplets they’re expelling, and many scientists now think that’s how most people become infected with the virus. One reason is that a virus inside a freshly exhaled droplet is more likely to be alive and infectious than a virus that’s been sitting on a doorknob for several hours. The other reason is that, in close range, breathing in the air that someone else just breathed out is going to expose you to a higher quantity of virus particles — called the inoculum — than after the droplets disperse and fall to the ground.')
        st.write('As a result, social distancing has become one of the recommended ways to prevent transmission, the idea being that if you stay more than six feet away from someone, you won’t be hit by the majority of their exhaled droplets. Supporting this theory, most people catch the virus from someone they live with and presumably are in frequent close contact with. In one study from China, for example, an infected person had a 17.2% chance of spreading the virus to a family member who lived with them, but just a 2.6% chance of giving it to someone outside the home.')
        st.subheader('“I think people have this preconceived notion that if it’s airborne it’s like the measles or like smallpox where it only takes one viral particle to infect you, and this is almost certainly not the case with this coronavirus. Most coronaviruses are probably in the hundreds.”')
        st.write('However, there have been several documented instances of infections that don’t fit with droplet or surface spread because they happened even when people maintained their distance. Perhaps the most famous example is the choir rehearsal outside of Seattle, Washington, a superspreader event where 52 out of 61 people were infected during a two-and-half-hour practice. What’s notable about this case is that the singers maintained distance from each other and used plenty of hand sanitizer, per safety guidance at the time. Also, the infected person was presymptomatic, so they weren’t coughing or sneezing and projecting droplets further. Despite all this, one person was still able to infect 52 others.')
        st.write('A study conducted in hamsters in a lab (that’s right, it turns out hamsters are the best animals in which to study coronavirus spread) found similar results in a more controlled environment. The researchers showed that the animals could infect each other not only through direct contact when they were housed in the same cage, but also when they were separated in different cages in the same room. Based on these studies and other mounting evidence, many scientists began to believe that the virus is transmitted through droplets and aerosols, those tiny mistlike particles that can travel farther through air currents and remain afloat for longer.')
        st.header('Aerosol transmission has gradually gained acceptance')
        st.write('Despite these observations, some public health experts were initially reluctant to say that the virus is airborne, partly because they didn’t want to alarm the public. There are also debates between epidemiologists, virologists, and aerosol engineers about what the word airborne really means — whether the size of the particles or their behavior (how quickly they fall to the ground, whether they can be carried on a gust of air) matters more, and what questions must be answered before a disease can be defined as such.')
        st.write('As surprising as it may sound, by comparison, the novel coronavirus is not very contagious. Each person who gets infected with SARS-CoV-2 will, on average, spread it to two or three other people. A person with measles will infect 15 others. WHO initially cited the coronavirus’s relatively low infectious rate as a reason why it couldn’t be spread through the air.')
        st.write('It wasn’t until a public outcry from over 200 scientists that the WHO finally conceded in July that aerosol transmission was possible.')
        st.write('So if the novel coronavirus is airborne, why isn’t it as contagious as measles? One reason could be that measles is a hardier virus (remember that SARS-CoV-2 is relatively fragile) and can survive longer in those tiny aerosols. Another potential difference is the infectious dose — the amount of virus required to start an infection. Scientists still don’t know exactly how much of the novel coronavirus is needed to make someone sick, but it’s likely higher than conventional airborne viruses.')
        st.write('Another question that needed to be answered before many public health experts could accept that SARS-CoV-2 was airborne was whether it could even survive in those smaller aerosol particles. Some viruses can’t because they dry up too quickly without a larger liquid droplet to support them. However, many scientists feel this issue has been put to rest with two recent papers (which have yet to be peer-reviewed) that provide what some have called the “smoking gun” for aerosol transmission: live, replicating virus collected from the air of Covid-19 patient hospital rooms.')
        st.header('How to protect yourself from all transmission routes')
        st.write('By now, most scientists and public health experts agree that SARS-CoV-2 can be spread by both droplets and aerosols, particularly in close range, although no one knows which is the dominant route of transmission.')
        st.write('What matters more is whether people know how to properly protect themselves from the virus. Fortunately, the prevention steps for both transmission routes are largely the same: keep your distance and wear a mask. Evidence of the importance of masks, in particular, has been mounting, not only because they trap outgoing particles from escaping, which protects others, but also because they block larger incoming particles from getting into a person’s airways, protecting the mask wearer themselves. And even if some viral particles do get through, the viral dose will still be much smaller, so the person will be less likely to get seriously ill')
        st.write('Aerosol transmission does increase the importance of one additional protective step, which is proper ventilation and air filtration. Airflow, either introducing new air into a room or filtering the existing air, can disperse and dilute any infectious aerosol particles, reducing a person’s potential exposure. Being outdoors is the ultimate ventilation, and for months public health officials have recommended that people socialize outside rather than in. However, with winter and colder temperatures coming, indoor air filtration and adherence to masks will become even more important.')
        st.subheader('Armed with this knowledge, think about how you can make fall and winter safer, both physically and mentally. Instead of buying another can of Lysol, maybe invest in an air purifier, more comfortable two-ply cloth masks, or even an outdoor fire pit or space heater. Be prepared to meet friends outside in colder temperatures or insist upon masks, even in your home. We’ve still got a long way to go before we can declare victory over the novel coronavirus, but at least we know more now than we did six months ago. And you don’t have to sanitize your apples anymore.')
        st.header('A word of Advice')
        st.write('The COVID-19 pandemic has demonstrated the interconnected nature of our world — and that no one is safe until everyone is safe. Only by acting in solidarity can communities save lives and overcome the devastating socio-economic impacts of the virus.')


    elif option=='Developer':
        html_temp = """
        <div style = "background-color: Cyan; padding: 10px;">
            <center><h1>Developer Section</h1></center>
        </div><br>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        st.title('Prepared by:-')
        st.header('SAURAV BORAH')
        st.subheader('Source Code:-')
        st.write('https://github.com/SAURAVBORAH22/covid-19-deep-analysis-')
        st.subheader('I have also written a blog. Please have a look:-')
        st.write('https://medium.com/cse-association-srm/covid-19-pandemic-in-india-80cff1056923')
        st.subheader('Follow me on LinkedIn :-')
        st.write('https://www.linkedin.com/in/saurav-borah-a7751818b/')


if __name__ == '__main__':
    main()