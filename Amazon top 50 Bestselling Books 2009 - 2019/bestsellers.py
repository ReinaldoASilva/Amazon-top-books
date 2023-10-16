# Importando Bibliotecas
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


# Visualize dataset
bestsellers = pd.read_csv('/Users/reinaldoblack/Documents/documentos/github/Amazon-top-books/Amazon top 50 Bestselling Books 2009 - 2019/bestsellers with categories.csv')

# Understanding the dataset

bestsellers.describe()

bestsellers.info()

bestsellers.shape

bestsellers.head()

# Null Values
bestsellers.isnull().sum(axis=0)

bestsellers['Reviews'].sum()

# Visualize the yers
print(bestsellers['Year'].unique())

# View max and min price
print(bestsellers['Price'].describe().loc[['max', 'min']])

# Books with price >= 100usd
bestsellers[bestsellers['Price']>=100][['Name', 'Author', 'Price']].drop_duplicates()
# We only have one book with a value greater than or equal to 100usd

# Books with price = 0 usd
bestsellers[bestsellers['Price']==0][['Name','Author','Price']].drop_duplicates()
# we only have 9 books with a value equal to 0 usd

# What kind of genres do we have?
genre = bestsellers['Genre'].value_counts(normalize=True)

plt.figure(figsize=(8,8))
plt.pie(genre.values, labels=genre.index, autopct='%1.1f%%')
plt.title('Genrer')
plt.axis('equal')
plt.show();

# What kind of genres do we have?
genre = bestsellers['Genre'].value_counts(normalize=True)
# How is the Numerical data Distributed?
for col in bestsellers.columns[2:5]:
    bestsellers[col].plot(kind = 'hist', bins=20, figsize=(16,5), edgecolor="#e28743",color ="#eab676")
    plt.axvline(bestsellers[col].mean(), c="#81200c", ls='-.', label= 'mean', lw=2, alpha=0.6)
    plt.axvline(bestsellers[col].median(), c="#1e81b0", ls='--', label='median',lw=2, alpha=0.6)
    plt.xlabel(col, fontsize=15)
    plt.title('Frequenci Distribution of'+" " +col, fontsize = 15, loc='left')
    plt.legend()
    plt.show()

# Lowest Rated book
lowestRatingBook = bestsellers[bestsellers["User Rating"] == bestsellers["User Rating"].min()]
lowestRatingBook['Genre'].value_counts()

#  The book you had the lowest assessment was The Casual Vacancy with 3.3


# highest Rated book
highRatingBook = bestsellers[bestsellers["User Rating"] == bestsellers["User Rating"].max()].drop_duplicates("Name")
highRatingBook['Genre'].value_counts()


# Maximum Reviews for a book
bestsellers[bestsellers["Reviews"] == bestsellers["Reviews"].max()]


# Minimum Reviews for a book
bestsellers[bestsellers["Reviews"] == bestsellers["Reviews"].min()]

# How has Average User Rating, Total Reviews an Average Price of books changed over the years?
bestsellers.groupby(["Year"]).agg({"User Rating":"mean","Reviews":["sum"], "Price":["sum"]}).transpose()

# Year-wise data of Average User Rating, Total Reviews and Average Price of books
bestsellers.groupby(["Year"]).agg({"User Rating":"mean","Reviews" :["sum"],"Price":["mean"]}).plot(subplots = True,                                                                                                                                                                                    figsize = (18,12), marker= "o", 
                                                                                          ls = "--", lw =2,
                                                                                         color = ["#1e81b0","#81200c","#e28743"],
                                                                                         title=["Mean User Rating","Number of Reviews","Mean Price of a book"])

plt.suptitle("Year-wise data of Average User Rating, Total Reviews and Average Price of books", fontsize =20)


# Genre Wise Distribution of Data
for col in bestsellers.columns[2:5]:
    plt.figure(figsize=(18,5))
    sns.boxplot(data = bestsellers, x=col, y ="Genre", palette=["#e28743","#81200c"])
    plt.title(" Genre-wise Distribution of"+ " " +  col, fontsize= 18)
    plt.xlabel(col,fontsize = 15)
    plt.ylabel("Genre", fontsize=15)
    plt.show()


# Year wise + Genre wise Distribution

for col in bestsellers.columns[2:5]:
    plt.figure(figsize=(18,8))
    sns.barplot(data=bestsellers, x="Year", y=col, hue="Genre", palette=["#e28743","#81200c"],errorbar=None)
    plt.legend(loc="upper left")
    plt.title("Genre-Wise Distribution of" + " " +  col + "(2009-2019)", fontsize=18)
    plt.xlabel("Year", fontsize=15)
    plt.ylabel(col, fontsize=15)
    plt.show()


# Average mean of no fiction
average_mean_no_fiction = bestsellers.groupby("Genre")["Price"].mean()
print(average_mean_no_fiction)






# Filter the dataframe by the genre "fiction"
fiction_df = bestsellers[bestsellers["Genre"] == "Fiction"]

# Get the list of available years
years_fiction_df = fiction_df['Year'].unique()
years_fiction_df.sort()

top5_livros_por_ano = []

# Loop pelos anos
for ano in years_fiction_df:
    # Filtrar o DataFrame pelo ano atual
    df_ano = fiction_df[fiction_df["Year"] == ano]

    # Obter os top 5 livros do ano atual
    top5_ano = df_ano.nlargest(5, 'User Rating')  # Substitua 'Column' pelo nome da coluna que deseja usar para classificar os livros

    # Adicionar os top 5 livros do ano atual à lista de top 5 livros por ano
    top5_livros_por_ano.append((ano, top5_ano["Name"].tolist()))

# Exibir os top 5 livros de cada ano
print("Top 5 livros por ano:")
for ano, livros in top5_livros_por_ano:
    print(f"Ano: {ano}")
    for livro in livros:
        print(livro)
    print()






# Encontrar os livros repetidos
anos_sucesso = {}

for ano, livros in top5_livros_por_ano:
    for livro in livros:
        if livro in anos_sucesso:
            anos_sucesso[livro].append(ano)
        else:
            anos_sucesso[livro] = [ano]

print("Livros repetidos em mais de um ano:")
for livro, anos in anos_sucesso.items():
    if len(anos) > 1:
        print(f"Livro: {livro} (Sucesso nos anos: {', '.join(map(str, anos))})")

# Dicionário para armazenar os top 5 livros por ano
summary = {
    2009: [{ 
            "Name" : "Diary of a Wimpy Kid The Last Straw (Livro 3)",
            "Age_Group" : "From 8 years",
            "Summary" : "In this third book in the Diary of a Wimpy Kid series, Greg Heffley continues to face the difficulties of adolescence. He is determined to become a more mature teenager, but ends up getting involved in several funny and embarrassing situations. The book portrays the struggles and challenges Greg faces as he tries to fit in at school and deal with his family's expectations."
        },       

            { 
            "Name" : "Dog Days",
            "Age_Group" : "From 8 years",
            "Summary" : "In the fourth book in the Diary of a Wimpy Kid series, Greg Heffley is on summer vacation and hopes to enjoy days full of fun and adventure. However, his expectations are dashed when he realizes that the summer season is not as exciting as he imagined. Greg faces boredom, confusion, and challenges as he tries to find ways to have fun during the holidays.",
        },       

            {
            "Name" : "The Help (A Resposta)", 
            "Age_Group" : "From 18 years",
            "Summary" : "Set in the 1960s, The Help is a novel written by Kathryn Stockett. The book portrays the lives of three different women, two of them black maids and the third a young white woman aspiring to be a writer. Together, they embark on a secret project to write a book that exposes the experiences of domestic workers in the segregated South of the United States. The book addresses issues of race, discrimination, and complex relationships in a troubled time in American history.",
        },
            
            {
            "Name" : "The Last Olympian",
            "Age_Group" : "From 10 years",
            "Summary": "(Percy Jackson and the Olympians, Book 5) This is the fifth book in the Percy Jackson and the Olympians series, written by Rick Riordan. The book follows the adventures of Percy Jackson, a demigod son of Poseidon, as he prepares for the final battle against the gods of Olympus. Percy and his friends face epic challenges, betrayals, and thrilling battles as they fight to save the world from destruction.",
        },
           
            {
            "Name" :"Watchmen",
            "Age_Group" : "From 18 years",
            "Summary" : "Watchmen is a graphic novel written by Alan Moore and illustrated by Dave Gibbons. Set in an alternate reality where superheroes are an integral part of society, the story follows a group of retired heroes who come together to investigate the murder of one of their former colleagues. Watchmen explores complex themes such as morality, power, politics, and personal identity, while delving into the lives and motivations of the main characters."
        
    }],

    2010: [{

            "Name" : "Percy Jackson and the Olympians Paperback Boxed Set (Books 1-3)",
            "Age_Group" : "From 10 years",
            "Summary" : "Humans and half-bloods alike agree—Percy Jackson and the Olympians is a series fit for heroes! Re-live the adventure from the beginning with this boxed set of the first three books.   The Lightning Thief:\
        Percy Jackson is a good kid, but he can’t seem to focus on his schoolwork or control his temper. When his mom tells him the truth about where he came from, she takes him to the one place he’ll be safe—Camp Half-Blood, a summer camp for demigods (on Long Island). There, Percy learns that the father he never knew is actually Poseidon, God of the Sea. Soon Percy finds himself caught up in a mystery that could lead to disastrous consequences. Together with his friends—a satyr and other the demigod daughter of Athena—Percy sets out on a quest to reach the gates of the Underworld (located in a recording studio in Hollywood) and prevent a catastrophic war between the gods.\
        The Sea of Monsters:\
        After a summer spent trying to prevent a catastrophic war among the Greek gods, Percy Jackson finds his seventh-grade school year unnervingly calm. But things don’t stay quiet for long. Percy soon discovers there is trouble at Camp Half-Blood: the magical borders which protect Half-Blood Hill have been poisoned by a mysterious enemy, and the only safe haven for demigods is on the verge of being overrun by mythological monsters. To save the camp, Percy needs the help of his best friend, Grover, who has been taken prisoner by the Cyclops Polyphemus on an island somewhere in the Sea of Monsters—the dangerous waters Greek heroes have sailed for millennia—only today, the Sea of Monsters goes by a new name: the Bermuda Triangle. Now Percy and his friends must retrieve the Golden Fleece from the Island of the Cyclopes by the end of the summer or Camp Half-Blood will be destroyed. But first, Percy will learn a stunning new secret about his family—one that makes him question whether being claimed as Poseidon’s son is an honor or simply a cruel joke...\
        The Titan’s Curse:\
        When Percy Jackson receives a distress call from his friend Grover, he immediately prepares for battle. He knows he'll need his powerful demigod allies, Annabeth and Thalia, at his side; his trusty bronze sword Riptide; and... a ride from his mom. The demigods race to the rescue, to find that Grover has made an important discovery: two new powerful half-bloods whose parentage is unknown. But that's not all that awaits them. The Titan lord, Kronos, has set up his most devious trap yet, and the young heroes have unwittingly fallen prey. Hilarious and action-packed, this third adventure in the series finds Percy faced with his most dangerous challenge so far: the chilling prophecy of the Titan's curse.\
        synopsis may belong to another edition of this title."
        },

            {
            "Name" : "The Lost Hero (Heroes of Olympus, Book 1)",
            "Age_Group" : "From 10 years",
            "Summary" : "Rick Riordan, the best-selling author of the Percy Jackson series, pumps up the action and suspense in The Lost Hero, the first book in The Heroes of Olympus series.\
        Riordan extends the franchise in a logical direction while maximizing the elements that made the first series so popular: irreverent heroes, plenty of tension-filled moments fighting monsters, and authentic classical mythology mixed in with modern life.—Horn Book \
        A New York Times best-seller \
        A spin-off of the blockbuster Percy Jackson and the Olympians series, but stands on its own \
        Combines Roman and Greek mythology \
        Told from the points of view of a diverse cast of demigods \
        Memorable characters, witty dialogue, and non-stop action have made this series popular across the globe \
        Perfect for middle grade listeners but can be enjoyed by older listeners, too \
        Jason has a problem. He doesnt remember anything before waking up on a school bus holding hands with a girl. Apparently she's his girlfriend Piper, his best friend is a kid named Leo, and they're all students in the Wilderness School, a boarding school for bad kids. What he did to end up here, Jason has no idea—except that everything seems very wrong. \
        Piper has a secret. Her father has been missing for three days, and her vivid nightmares reveal that he's in terrible danger. Now her boyfriend doesn't recognize her, and when a freak storm and strange creatures attack during a school field trip, she, Jason, and Leo are whisked away to someplace called Camp Half-Blood. What is going on? \
        Leo has a way with tools. His new cabin at Camp Half-Blood is filled with them. Seriously, the place beats Wilderness School hands down, with its weapons training, monsters, and fine-looking girls. What's troubling is the curse everyone keeps talking about, and that a camper's gone missing. Weirdest of all, his bunkmates insist they are all—including Leo—related to a god. \
        Fans of demigods, prophecies, and quests will be left breathless—and panting for Book Two." 
        },

            {
            "Name" : "The Ugly Truth (Diary of a Wimpy Kid, Book 5)",
            "Age_Group" : "From 8 years",
            "Summary" : "Greg Heffley has always been in a hurry to grow up. But is getting older really all it’s cracked up to be?\
        Greg suddenly finds himself dealing with the pressures of boy-girl parties, increased responsibilities, and even the awkward changes that come with getting older—all without his best friend, Rowley, at his side. Can Greg make it through on his own? Or will he have to face the “ugly truth”?"
        
    }],

    2011:[{
            "Name" : "Cabin Fever (Diary of a Wimpy Kid, Book 6)",
            "Age_Group" : "From 8 years",
            "Summary": "In Cabin Fever, book 6 of the Diary of a Wimpy Kid series from \
        chool property has been damaged, and Greg is the prime suspect. But the crazy thing is, he’s innocent. Or at least sort of.\
        The authorities are closing in, but when a surprise blizzard hits, the Heffley family is trapped indoors. Greg knows that when the snow melts he’s going to have to face the music, but could any punishment be worse than being stuck inside with your family for the holidays?"
        },

            {
            "Name" : "Go the F**k to Sleep",
            "Age_Group" : "From 18 years",
            "Summary" : "Go the Fk to Sleep is a bedtime book for parents who live in the real world, where a few snoozing kitties and cutesy rhymes don't always send a toddler sailing blissfully off to dreamland. Profane, affectionate, and radically honest, California Book Award-winning author Adam Mansbach's verses perfectly capture the familiar--and unspoken--tribulations of putting your little angel down for the night. In the process, they open up a conversation about parenting, granting us permission to admit our frustrations, and laugh at their absurdity.\
        With illustrations by Ricardo Cortes, Go the Fk to Sleep is beautiful, subversive, and pants-wettingly funny--a book for parents new, old, and expectant. You probably should not read it to your children.\
        Seriously, Just Go to Sleep, a children's book inspired by Go the F**k to Sleep and appropriate for kids of all ages, is also available, as well as Seriously, You Have to Eat for finicky ones everywhere."
        }, 

            {
            "Name" : "The Hunger Games Trilogy Boxed Set (1)",
            "Age_Group" : "From 8 years",
            "Summary" : "The stunning Hunger Games trilogy complete in the form of a boxed set. The extraordinary, ground breaking New York Times bestsellers The Hunger Games and Catching Fire, along with the third book in The Hunger Games trilogy by Suzanne Collins, Mockingjay, are available for the first time ever in a beautiful boxset edition. Stunning, gripping, and powerful."
    
    }],

    2012:[{         
            "Name" : "Goodnight, Goodnight Construction Site (Hardcover Books for Toddlers, Preschool Books for Kids)",
            "Age_Group" : "From 8 years",
            "Summary" : "The #1 New York Times bestselling children's bookAs the sun sets behind the big construction site, all the hardworking trucks get ready to say goodnight. One by one, Crane Truck, Cement Mixer, Dump Truck, Bulldozer, and Excavator finish their work and lie down to rest—so they'll be ready for another day of rough and tough construction play! With irresistible artwork by bestselling illustrator Tom Lichtenheld and sweet, rhyming text, this construction book for kids will have truck lovers of all ages begging for more.Can't get enough of these tough trucks? The long-awaited sequel in this bestselling book series, Mighty, Mighty, Construction Site, is now available!"
        },

            {
            "Name" : "Oh, the Places You'll Go!",
            "Age_Group" : "From 3 years",
            "Summary" : "A perennial favorite, Dr. Seuss’s wonderfully wise graduation speech is the perfect send-off for children starting out in the world, be they nursery school, high school, or college grads! From soaring to high heights and seeing great sights to being left in a Lurch on a prickle-ly perch, Dr. Seuss addresses life’s ups and downs with his trademark humorous verse and illustrations, while encouraging readers to find the success that lies within. In a starred review, Booklist notes: “Seuss’s message is simple but never sappy: life may be a ‘Great Balancing Act,’ but through it all ‘There’s fun to be done."
        },

            {
            "Name" : "The Hunger Games Trilogy Boxed Set (1)",
            "Age_Group" : "From 13 years",
            "Summary" : "The stunning Hunger Games trilogy complete in the form of a boxed set.The extraordinary, ground breaking New York Times bestsellers The Hunger Games and Catching Fire, along with the third book in The Hunger Games trilogy by Suzanne Collins, Mockingjay, are available for the first time ever in a beautiful boxset edition. Stunning, gripping, and powerful. "
        },

            {
            "Name" : "The Mark of Athena (Heroes of Olympus, Book 3)",
            "Age_Group" : "From 10 years",
            "Summary" : "Annabeth felt as if someone had draped a cold wash cloth across her neck. She heard that whispering laughter again, as if the presence had followed her from the ship. She looked up at the Argo II. Its massive bronze hull glittered in the sunlight"
        },

            {
            "Name" : "The Serpent's Shadow (The Kane Chronicles, Book 3)",
            "Age_Group" : "From 10 years",
            "Summary" : "Carter and Sadie Kane, descendants of the magical House of Life, are in pretty big trouble. Despite their bravest efforts, Apophis, the giant snake of Chaos, is still threatening to plunge the world into eternal darkness. Now the Kanes must do something no magician has ever managed - defeat Apophis himself. No pressure there then."
    }],
    

    2013:[{
            "Name" : "Rush Revere and the Brave Pilgrims: Time-Travel Adventures with Exceptional Americans (1)",  
            "Age_Group" : "From 8 years",
            "Summary" : "The #1 New York Times bestselling children's bookAs the sun sets behind the big construction site, all the hardworking trucks get ready to say goodnight. One by one, Crane Truck, Cement Mixer, Dump Truck, Bulldozer, and Excavator finish their work and lie down to rest—so they'll be ready for another day of rough and tough construction play! With irresistible artwork by bestselling illustrator Tom Lichtenheld and sweet, rhyming text, this construction book for kids will have truck lovers of all ages begging for more.Can't get enough of these tough trucks? The long-awaited sequel in this bestselling book series, Mighty, Mighty, Construction Site, is now available!"    
        },

            {
            "Name" : "The Legend of Zelda: Hyrule Historia",  
            "Age_Group" : "From 18 years",
            "Summary" : "Dark Horse Books and Nintendo team up to bring you The Legend of Zelda: Hyrule Historia, containing an unparalleled collection of historical information on The Legend of Zelda franchise. This handsome hardcover contains never-before-seen concept art, the full history of Hyrule, the official chronology of the games, and much more! Starting with an insightful introduction by the legendary producer and video-game designer of Donkey Kong, Mario, and The Legend of Zelda, Shigeru Miyamoto, this book is crammed full of information about the storied history of Link's adventures from the creators themselves! As a bonus, The Legend of Zelda: Hyrule Historia includes an exclusive comic by the foremost creator of The Legend of Zelda manga — Akira Himekawa!"
        }, 

            {
            "Name" : "The Very Hungry Caterpillar",  
            "Age_Group" : "From 3 years",
            "Summary" : "The Very Hungry Caterpillar is a beloved children's book written and illustrated by Eric Carle. It tells the story of a caterpillar who starts off small and hungry, but goes on an eating spree, consuming various foods each day of the week. As the caterpillar eats, it grows bigger and bigger until it eventually forms a cocoon. Inside the cocoon, the caterpillar undergoes a transformation and emerges as a beautiful butterfly.\
        The book not only entertains children with its engaging story, but also provides educational elements. It introduces concepts such as the days of the week, different types of food, and the life cycle of a butterfly. The vibrant and colorful illustrations by Eric Carle captivate young readers and bring the story to life.\
        The Very Hungry Caterpillar has become a classic in children's literature, captivating generations of readers. Its simple yet captivating narrative, combined with the interactive element of die-cut pages that show the caterpillar's journey, keeps children engaged and encourages their participation in the story.\
        Through its tale of growth, transformation, and the wonders of nature, the book conveys important lessons to children. It teaches them about the consequences of overindulgence, the beauty of patience, and the rewards of self-care. With its timeless appeal and delightful illustrations, The Very Hungry Caterpillar continues to be cherished as a cherished reading experience for young children."
        
    }],

    2014:[{
            "Name" : "Little Blue Truck",
            "Age_Group" : "From 3 years",
            "Summary" : "Beep! Beep! Meet Blue! Filled with truck sounds and animal noises, Little Blue Truck is a rollicking homage to the power of friendship and the rewards of helping others.\
        A muddy country road is no match for this little pick-up--that is, until he gets stuck while pushing a dump truck out of the muck.\
        Luckily, Blue has made a pack of farm animal friends along his route. And they're willing to do whatever it takes to get their pal back on the road.\
        Little Blue Truck is a joyful cacophony of animal and truck sounds that will have youngsters beeping and quacking--and begging for one more go-round!\
        Along the way, readers see that it pays to be kind to our animal friends. If we show a friendly respect to others, we're more likely to get help when we're, say, stuck in the muck in a truck!"
        },       

            {
            "Name" : "Rush Revere and the First Patriots: Time-Travel Adventures With Exceptional Americans (2)", 
            "Age_Group" : "From 8 years",
            "Summary" : "From America's #1 radio talk show host and #1 New York Times bestselling author, the second book in a series for young readers with a history teacher who travels back in time to have adventures with exceptional Americans.\
        Rush Revere rides again! Saddle up with Rush Limbaugh's really good pal for a new time-travel adventure.\
        Whoa there, young historians! Before we go rush, rush, rushing off anywhere, I'd like a moment. I'm Liberty, Rush Revere's loquacious equine companion--his trusty talking horse! Always at the ready to leap from the twenty-first century into America's past, that's me. When he says 'Let's go!' I'm so there. I'm jazzed, I'm psyched, I'm--\
        Ah, excuse me, Liberty?\
        Yeah, Rush?\
        Usually you say oh no, not again! and 'while we're in colonial Boston, can I try the baked beans?\
        Okay, fine--you do the talking. I'll just be over here, if you need me....\
        Well, he's sulking now, but I couldn't be your tour guide across time without Liberty! His name says it all: the freedom we celebrate every July Fourth with fireworks and hot dogs (and maybe some of those baked beans). But how did America get free? How did thirteen newborn colonies tell the British king where he could stick his unfair taxes?\
        Jump into the bustling streets of Boston in 1765, where talk of revolution is growing louder. I said LOUDER. You'll have to SHOUT to be heard over the angry cries of Down with the king! and Repeal the Stamp Act! that fill the air. You'll meet fierce supporters of liberty like Samuel Adams, Benjamin Franklin, and my idol, Paul Revere, as they fearlessly defy British rule. It's an exciting, dangerous, turbulent, thrilling time to be an American...and exceptional young patriots like you won't want to miss a minute. Let's ride!"
        },            

            {
            "Name" : "Diary of a Wimpy Kid: The Long Haul", 
            "Age_Group" : "From 8 years",
            "Summary" : "A family road trip is supposed to be a lot of fun . . . unless, of course, you re theHeffleys.The journey starts off full of promise, then quickly takes several wrong turns.Gas station bathrooms, crazed seagulls, a fender bender, and a runaway pig not exactly Greg Heffley s idea of a good time.But even the worst road trip can turn into an adventure and this is one the Heffleyswon t soon forget."
    
    }],

    2015:[{
            "Name" : "Dear Zoo: A Lift-the-Flap Book", 
            "Age_Group" : "From 8 years",
            "Summary" : "is a beloved children's book by Rod Campbell that engages young readers with its interactive flaps. The story revolves around a child who writes to the zoo seeking a pet. Each page features a flap that children can lift to discover a different animal sent by the zoo. However, each animal proves unsuitable for various reasons, creating anticipation and excitement for what animal will come next. Finally, the zoo sends the perfect pet, a puppy, bringing joy to both the child and readers.\
        Through the book's interactive nature, children actively participate by lifting the flaps to uncover hidden animals. This element of surprise encourages engagement and promotes fine motor skills development. The repetitive and rhythmic text structure adds to the book's appeal, making it an enjoyable read-aloud experience for parents and caregivers. The colorful illustrations by Rod Campbell captivate young readers, helping them visualize the animals and enhancing their imagination."
        } ,   

            {
            "Name" : "Giraffes Can't Dance", 
            "Age_Group" : "From 8 years",
            "Summary" : "Giraffes Can't Dance is a touching tale of Gerald the giraffe, who wants nothing more than to dance. With crooked knees and thin legs, it's harder for a giraffe than you would think. Gerald is finally able to dance to his own tune when he gets some encouraging words from an unlikely friend.\
        With light-footed rhymes and high-stepping illustrations, this tale is gentle inspiration for every child with dreams of greatness."
        },

            {
            "Name" : "Love You Forever", 
            "Age_Group" : "From 8 years",
            "Summary" : "A young woman holds her newborn son \
        And looks at him lovingly.\
        Softly she sings to him:\
        I'll love you forever\
        I'll like you for always\
        As long as I'm living\
        My baby you'll be.\
        So begins the story that has touched the hearts of millions worldwide. Since publication in l986, Love You Forever has sold more than 36 million copies in paperback and the regular hardcover edition (as well as hundreds of thousands of copies in Spanish and French).\
        Firefly Books is proud to offer this sentimental favorite in a variety of editions and sizes:"
      
    }],

    2016:[{
            "Name" :  "Harry Potter and the Chamber of Secrets: The Illustrated Edition (Harry Potter, Book 2)",
            "Age_Group" : "From 8 years",
            "Summary" : "The Dursleys were so mean and hideous that summer that all Harry Potter wanted was to get back to the Hogwarts School for Witchcraft and Wizardry. But just as he's packing his bags, Harry receives a warning from a strange, impish creature named Dobby who says that if Harry Potter returns to Hogwarts, disaster will strike.And strike it does. For in Harry's second year at Hogwarts, fresh torments and horrors arise, including an outrageously stuck-up new professor, Gilderoy Lockhart, a spirit named Moaning Myrtle who haunts the girls' bathroom, and the unwanted attentions of Ron Weasley's younger sister, Ginny.But each of these seem minor annoyances when the real trouble begins, and someone -- or something -- starts turning Hogwarts students to stone. Could it be Draco Malfoy, a more poisonous rival than ever? Could it possibly be Hagrid, whose mysterious past is finally told? Or could it be the one everyone at Hogwarts most suspects... Harry Potter himself?"
        },
              
            {
            "Name" : "Harry Potter and the Sorcerer's Stone: The Illustrated Edition (Harry Potter, Book 1)",  
            "Age_Group" : "From 8 years",
            "Summary" : "For the first time, J.K. Rowling's beloved Harry Potter books will be presented in lavishly illustrated full-color editions. Award-winning artist Jim Kay has created over 100 stunning illustrations, making this deluxe format a perfect gift for a child being introduced to the series and for dedicated fans.Harry Potter has never been the star of a Quidditch team, scoring points while riding a broom far above the ground. He knows no spells, has never helped to hatch a dragon, and has never worn a cloak of invisibility.All he knows is a miserable life with the Dursleys, his horrible aunt and uncle, and their abominable son, Dudley - a great big swollen spoiled bully. Harry's room is a tiny closet at the foot of the stairs, and he hasn't had a birthday party in eleven years.But all that is about to change when a mysterious letter arrives by owl messenger: a letter with an invitation to an incredible place that Harry - and anyone who reads about him - will find unforgettable."
        },

            {
            "Name" : "The Wonderful Things You Will Be", 
            "Age_Group" : "From 3 years",
            "Summary" : "The New York Times bestseller that celebrates the dreams, acceptance, and love that parents have for their children . . . now and forever. This is the perfect heartfelt gift for kids of all ages, plus a great choice for baby showers, birthdays, graduations, and other new beginnings!\
        From brave and bold to creative and clever, Emily Winfield Martin's rhythmic rhyme expresses all the loving things that parents think of when they look at their children. With beautiful, lush illustrations and a stunning gatefold that opens at the end, this is a book that families will love reading over and over.\
        The Wonderful Things You Will Be has a loving and truthful message that will endure for lifetimes and makes a great gift to the ones you love for any occasion."
    
    }],

    2017:[{
            "Name" : "Brown Bear, Brown Bear, What Do You See?",
            "Age_Group" : "From 3 years",
            "Summary" : "A big happy frog, a plump purple cat, a handsome blue horse, and a soft yellow duck--all parade across the pages of this delightful book. Children will immediately respond to Eric Carle's flat, boldly colored collages. Combined with Bill Martin's singsong text, they create unforgettable images of these endearing animals."
        },
            
            {
            "Name" : "Dog Man: A Tale of Two Kitties: From the Creator of Captain Underpants (Dog Man #3)", 
            "Age_Group" : "From 8 years",
            "Summary" :  "A cute kitten disrupts Petey's plans in the third Dog Man book from worldwide bestselling author and artist Dav Pilkey.\
        He was the best of dogs... He was the worst of dogs... It was the age of invention... It was the season of surprise... It was the eve of supa sadness... It was the dawn of hope... Dog Man hasn't always been a paws-itive addition to the police force. While he can muzzle miscreants, he tends to leave a slick of slobber in his wake! This time, Petey the Cat's dragged in a tiny bit of trouble -- a double in the form of a kitten clone. Dog Man will have to work twice as hard to bust these furballs and remain top dog!\
        Dav Pilkey's wildly popular Dog Man series appeals to readers of all ages and explores universally positive themes, including empathy, kindness, persistence, and the importance of being true to one's self."
        },

            {
            "Name" : "Harry Potter and the Prisoner of Azkaban: The Illustrated Edition (Harry Potter, Book 3)", 
            "Age_Group" : "From 8 years",
            "Summary" : "The third book in the bestselling Harry Potter series, now illustrated in glorious full color by award-winning artist Jim Kay!\
        scaped, leaving only two clues as to where he might be headed: Harry Potter's defeat of You-Know-Who was Black's downfall as well. And the Azkaban guards heard Black muttering in his sleep, He's at Hogwarts . . . he's at Hogwarts.Harry Potter isn't safe, not even within the walls of his magical school, surrounded by his friends. Because on top of it all, there may well be a traitor in their midst."
        
    }],

    2018:[{
            "Name" : "Dog Man and Cat Kid: From the Creator of Captain Underpants (Dog Man #4)",
            "Age_Group" : "From 8 years",
            "Summary" : "Hot diggity dog! Dog Man is back -- and this time he's not alone. The heroic hound with a real nose for justice now has a furry feline sidekick, and together they have a mystery to sniff out! When a new kitty sitter arrives and a glamorous movie starlet goes missing, it's up to Dog Man and Cat Kid to save the day! Will these heroes stay hot on the trail, or will Petey, the World's Most Evil Cat, send them barking up the wrong tree?\
        Dav Pilkey's wildly popular Dog Man series appeals to readers of all ages and explores universally positive themes, including empathy, kindness, persistence, and the importance of being true to one's self."
        },

            {
            "Name" : "Dog Man: Brawl of the Wild: From the Creator of Captain Underpants (Dog Man #6)", 
            "Age_Group" : "From 8 years",
            "Summary" : "The heroic hound is send to jail in the sixth Dog Man book from worldwide bestselling author and artist Dav Pilkey.\
        Is Dog Man bad to the bone? The canine cop is sent to the pound for a crime he didn't commit! While his pals work to prove his innocence, Dog Man struggles to find his place among dogs and people. Being a part of both worlds, will he ever fully fit in with one?\
        av Pilkey's wildly popular Dog Man series appeals to readers of all ages and explores universally positive themes, including empathy, kindness, persistence, and the importance of being true to one's self."
        },

            {
            "Name" : "Dog Man: Lord of the Fleas: From the Creator of Captain Underpants (Dog Man #5)", 
            "Age_Group" : "From 8 years",
            "Summary" :  "The Supa Buddies convene to deal with some new villains in the fifth Dog Man book from worldwide bestselling author and artist Dav Pilkey.\
        When a fresh bunch of baddies bust up the town, Dog Man is called into action -- and this time he isn't alone. With a cute kitten and a remarkable robot by his side, our heroes must save the day by joining forces with an unlikely ally: Petey, the World's Most Evil Cat. But can the villainous Petey avoid vengeance and venture into virtue?\
        Dav Pilkey's wildly popular Dog Man series appeals to readers of all ages and explores universally positive themes, including empathy, kindness, persistence, and the importance of being true to one's self."
        },

            {
            "Name" : "Last Week Tonight with John Oliver Presents A Day in the Life of Marlon Bundo (Better Bundo Book, LGBT Childrens Book)", 
            "Age_Group" : "From 3 years",
            "Summary" : "HBO's Emmy-winning Last Week Tonight with John Oliver presents a children's book called Last Week Tonight with John Oliver Presents a Day in the Life of Marlon Bundo, which tells the heartwarming story of a Very Special boy bunny who falls in love with another boy bunny. The book explores themes of tolerance, same-sex marriage, and democracy, and 100 percent of the proceeds are donated to The Trevor Project and AIDS United.\
       This #1 New York Times Bestseller and #1 Amazon Bestseller has captured the nation's attention with its powerful message and charming illustrations. It is a bedtime story that doubles as a vital LGBTQ book for children and their grownups, promoting the idea that love is love. The audiobook version, narrated by Jim Parsons and featuring special guests like Jesse Tyler Ferguson and RuPaul, has also gained popularity."
    }],

    2019:[{
            "Name" : "Dog Man: Fetch-22: From the Creator of Captain Underpants (Dog Man #8)",
            "Age_Group" : "From 8 years",
            "Summary" : "Howl with laughter with Dog Man, the #1 New York Times bestselling series from Dav Pilkey, the creator of Captain Underpants! The heroic hound is send to jail in the sixth Dog Man book from worldwide bestselling author and artist Dav Pilkey.Is Dog Man bad to the bone? The canine cop is sent to the pound for a crime he didn't commit! While his pals work to prove his innocence, Dog Man struggles to find his place among dogs and people. Being a part of both worlds, will he ever fully fit in with one? Dav Pilkey's wildly popular Dog Man series appeals to readers of all ages and explores universally positive themes, including empathy, kindness, persistence, and the importance of being true to one's self."
        },

            {
            "Name" : "Dog Man: For Whom the Ball Rolls: From the Creator of Captain Underpants (Dog Man #7)", 
            "Age_Group" : "From 8 years",
            "Summary" :"Petey learns what it means to do good in the seventh Dog Man book from worldwide bestselling author and artist Dav Pilkey.\
        The Supa Buddies have been working hard to help Dog Man overcome his bad habits. But when his obsessions turn to fears, Dog Man finds himself the target of an all-new supervillain! Meanwhile, Petey the Cat has been released from jail and starts a new life with Li'l Petey. But when Petey's own father arrives, Petey must face his past and fight for who he loves.\
        Dav Pilkey's wildly popular Dog Man series appeals to readers of all ages and explores universally positive themes, including empathy, kindness, persistence, and the importance of doing good."
        },

            {
             "Name" : "Harry Potter and the Goblet of Fire: The Illustrated Edition (Harry Potter, Book 4) (4)", 
             "Age_Group" : "From 8 years",
             "Summary" : "The fourth book in the beloved Harry Potter series, now illustrated in glorious full color by award-winning artist Jim Kay. With over 150 illustrations!\
        Harry Potter wants to get away from the pernicious Dursleys and go to the International Quidditch Cup with Hermione, Ron, and the Weasleys. He wants to dream about Cho Chang, his crush (and maybe do more than dream). He wants to find out about the mysterious event involving two other rival schools of magic, and a competition that hasn't happened for a hundred years. He wants to be a normal, fourteen-year-old wizard. Unfortunately for Harry Potter, he's not normal - even by wizarding standards. And in this case, different can be deadly.With over 150 dazzling illustrations from Jim Kay, this new fully illustrated edition of the complete and unabridged text of Harry Potter and the Goblet of Fire is sure to delight fans and first-time readers alike."  
    }],

}




age_count = {}  # Dicionário auxiliar para contar a quantidade de livros em cada faixa etária

for year in summary:
    books = summary[year]  # Obtém a lista de livros para o ano atual
    
    for book in books:
        age_group = book["Age_Group"]  # Obtém a faixa etária do livro
        
        # Verifica se a faixa etária já está no dicionário auxiliar, se não, adiciona com valor inicial 1
        if age_group not in age_count:
            age_count[age_group] = 1
        else:
            age_count[age_group] += 1  # Incrementa a contagem de livros para a faixa etária atual

# Ordena o dicionário age_count com base nos valores (quantidade de livros) em ordem decrescente
sorted_age_count = sorted(age_count.items(), key=lambda x: x[1], reverse=True)

# Imprime as faixas etárias destacadas do maior para o menor número de livros
for age_group, count in sorted_age_count:
    print("Faixa etária:", age_group)
    print("Quantidade de livros:", count)
    print("---")















# Criar um dicionário para armazenar os anos de sucesso de cada livro
anos_sucesso = {}

# Exibir os top 5 livros de cada ano
print("Top 5 livros por ano:")
for ano, livros in top5_livros_por_ano:
    print(f"Ano: {ano}")
    for livro in livros:
        nome_livro, genero = livro
        print(f"Livro: {nome_livro} - Gênero: {genero}")
        livro_tupla = tuple(livro)  # Converter a lista do livro em uma tupla
        if livro_tupla in anos_sucesso:
            anos_sucesso[livro_tupla].append(ano)  # Adicionar o ano à lista de anos de sucesso do livro
        else:
            anos_sucesso[livro_tupla] = [ano]  # Criar uma nova entrada no dicionário para o livro
    print()

# Encontrar os livros repetidos
print("Livros repetidos em mais de um ano:")
for livro, anos in anos_sucesso.items():
    if len(anos) > 1:
        nome_livro, genero = livro
        print(f"Livro: {nome_livro} - Gênero: {genero} (Sucesso nos anos: {', '.join(map(str, anos))})")


###################################################### Genero ideal para lançamento ###################################################


# Filtrar o DataFrame pelos top 5 livros mais vendidos em todos os anos
top5_df = bestsellers.groupby(["Year", "Genre"])["Name"].value_counts().groupby(level=[0, 1]).nlargest(5).reset_index(level=[0, 1, 2], drop=True)

# Calcular a contagem de ocorrências de cada tema
temas_contagem = top5_df.groupby("Genre").size().sort_values(ascending=False)

# Obter o tema mais ideal para lançar um livro
tema_ideal = temas_contagem.index[0]

print(f"O tema mais ideal para lançar um livro com base nos top 5 livros mais vendidos em todos os anos é: {tema_ideal}")








