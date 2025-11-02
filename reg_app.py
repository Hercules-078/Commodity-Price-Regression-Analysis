import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
##st.set_page_config(layout='wide',page_icon="Reg_analysis")

_,col2,_=st.columns([0.2,2,0.1])
with col2:
    st.title("Cross-Sector Commodity Price :red[Regression Analysis]",width='stretch')
st.divider()
st.sidebar.title("Sections")
def show_abstract():
    st.header(":blue[Abstract]")
    st.markdown(" The objective of this project is to investigate the relationships between commodities from diverse sectors (such as Metals, Energy, and Beverages) using linear regression analysis. Monthly price data for 17 different commodities was collected from 1995 to July 2025. After organizing the data in an Excel sheet, correlation coefficients were calculated for all pairs of commodities. The top six pairs with correlation scores above 0.63 were further analyzed using linear regression, and their R² values were calculated and presented graphically. Finally, the project explores potential (hypothetical) reasons behind strong inter-commodity relationships across different sectors, as well as possible explanations for the lack of correlation between certain commodities.")
    st.divider()

def show_methodology():
    st.header(":blue[Methodology]")
    st.subheader("Objective") 
    st.markdown("Commodities play a crucial role in the global economy, and their price movements are often inter connected due to shared production costs, global demand trends, and market dependencies.The primary objective of this project is to study and understand the interrelationships between commodities from diverse sectors such as Metals, Energy, and Beverages through statistical and regression analysis.By examining these relationships, this project aims to identify how the price of one commodity influences another and how various sectors are correlated over time.")
    st.markdown("Using historical monthly price data for 17 commodities ranging from January 1995 to July 2025, the project applies correlation and linear regression analysis to uncover meaningful associations. The top correlated pairs are analyzed in-depth to determine the strength and nature of their relationships using R² (coefficient of determination) and regression plots.")
    st.markdown("The findings of this analysis can provide valuable insights for economists, investors, and policymakers to predict commodity trends, assess risks, and make data-driven decisions in trading and investment strategies.")
    st.subheader("Commodities Overview")
    st.markdown("""The dataset includes 17 commodities representing diverse economic sectors such as energy, agriculture, metals, and natural resources. By analyzing these together, we can study how markets from different domains interact with each other — for instance, how energy prices like crude oil affect agricultural commodities such as wheat or rice, or how metal prices are connected to industrial or agricultural trends.

Below is an overview of each commodity and its relevance:

1. **Crude Oil**: The backbone of the energy sector; its price influences nearly all other markets due to transportation and production costs.

2. **Wheat**: A key food grain and global staple; sensitive to climate, demand, and energy-driven agricultural costs.

3. **Aluminum**: A vital industrial metal used in transport, packaging, and construction; linked to economic and energy fluctuations.

4. **Sugar**: A key agricultural and processed commodity influenced by global demand, weather conditions, and biofuel production.

5. **Bananas**: A major fruit export crop; prices depend on weather, logistics, and agricultural input costs.

6. **Rice**: A staple grain for over half the world’s population; its price reflects agricultural trends and monsoon performance.

7. **Beef**: A major protein source; influenced by feed costs, livestock production, and trade regulations.

8. **Chicken**: A fast-growing protein market; dependent on feed costs (linked to grains like corn and soy).

9. **Fish**: Represents marine and aquaculture sectors; sensitive to environmental and economic conditions.

10. **Coconut Oil**: Used in food, cosmetics, and energy; affected by tropical yields and substitute oils like palm or soybean.

11. **Cotton**: A key raw material for textiles; linked with agricultural inputs and global fashion demand.

12. **Rubber**: Industrial commodity used in tires and manufacturing; correlated with oil prices and industrial output.

13. **Iron Ore**: The foundation for steel production; its price is closely tied to industrial demand and global construction trends.

14. **Zinc**: An industrial metal used in galvanization and alloys; fluctuates with mining output and energy prices.

15. **Urea**: A nitrogen fertilizer; highly dependent on energy and agricultural markets.

16. **Plywood**: Reflects trends in construction, furniture, and housing sectors.

17. **Soybean Oil**: A multi-purpose agricultural product used in food and biofuel; affected by oil prices and crop yields.

By combining commodities from multiple sectors, we aim to uncover how global systems are intertwined — revealing how economic, industrial, and agricultural activities influence one another over long periods.""")
#////////////////////////////////////////////////////////////////////    
    st.subheader("Line Plot Visualization")
    st.markdown("To begin the analysis, we plotted time-series line plots for all 17 commodities over the 30-year period from 1995 to 2025. Each line represents the monthly price variation of a commodity, showing its trends, seasonal patterns, and volatility.")
    st.markdown("The line plots allow for a visual understanding of market dynamics. Some commodities, like crude oil and aluminum, exhibit sharp fluctuations reflecting global crises or industrial demand shifts. Agricultural commodities like rice, wheat, and sugar show periodic cycles tied to harvest seasons and climate variability. Meanwhile, livestock-based commodities such as beef and chicken show gradual upward trends, reflecting long-term global consumption growth.")
    st.markdown("""From the plots, several key observations emerged:

- Commodities within the same sector (like metals or food grains) might share similar movement patterns, suggesting sector-wide economic factors.

- Commodities from different sectors also display periodic synchronization, hinting at cross-sector influences — for example, rising energy prices increasing agricultural input costs, which in turn affect food prices.

- Price volatility varies significantly: energy commodities exhibit the highest fluctuations, while food and industrial goods display relatively stable trends.""")
    st.markdown(" ")
    
    df= pd.read_excel("Book2.xlsx")

    t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18=st.tabs(["Crude","Wheat","Aluminum","Sugar","Bananas","Rice","Beef","Chicken","Fish","Coconut oil","Cotton","Rubber","Iron Ore ","Zinc","Urea","Plywood","Soybean Oil","All"])
    with t1:
        st.line_chart(df,y="Crude Oil Prices",x="Date")
    with t2:
        st.line_chart(df,y="Soybean Oil Monthly Price  US Dollars per Metric Ton",x="Date")
    with t3:
        st.line_chart(df,y="Aluminum Monthly Price US Dollars per Metric Ton",x="Date")
    with t4:
        st.line_chart(df,y="Sugar US Dollars per Kilogram",x="Date")    
    with t5:
        st.line_chart(df,y="Bananas Price per Kg",x="Date")
    with t6:
        st.line_chart(df,y="Rice price US Dollars per Metric Ton",x="Date")
    with t7:
        st.line_chart(df,y="Beef US Dollars per Kilogram",x="Date")
    with t8:
        st.line_chart(df,y="chicken US Dollars per Kilogram",x="Date")
    with t9:
        st.line_chart(df,y="Fish US Dollars per Kilogram",x="Date")
    with t10:
        st.line_chart(df,y="Coconut oil Price per Metric Ton",x="Date")
    with t11:
        st.line_chart(df,y="Cotton Monthly Price US Dollars per Kilogram",x="Date")
    with t12:
        st.line_chart(df,y="Rubber Monthly Price US Dollars per Kilogram",x="Date")
    with t13:
        st.line_chart(df,y="Iron Ore Monthly Price US Dollars per Dry Metric Ton",x="Date")
    with t14:
        st.line_chart(df,y="Zinc Monthly Price US Dollars per Metric Ton",x="Date")
    with t15:
        st.line_chart(df,y="Urea Monthly Price US Dollars per Metric Ton",x="Date")
    with t16:
        st.line_chart(df,y="Plywood Monthly Price US cents per sheets",x="Date")
    with t17:
        st.line_chart(df,y="Soybean Oil Monthly Price  US Dollars per Metric Ton",x="Date")
    with t18:
        st.image("total.jpg")
    #////////////////////////////////////////////////////////////////////////
        
    st.subheader("HeatMap")
    st.markdown("""After visualizing the time-series data, we proceeded to a correlation analysis, presented through two heatmaps.

1. **Heatmap 1 – Full Correlation Matrix:**
                The first heatmap displays the correlation coefficients between every pair of the 17 commodities. Each cell represents how strongly the prices of two commodities move together, with values ranging from -1 to +1.

- High positive correlations (close to +1) indicate that both commodities move in the same direction.

- Negative correlations (close to -1) suggest that when one rises, the other tends to fall.

-  Values near 0 show weak or no relationship.

This heatmap reveals the broad interconnectedness across the global commodity market. For instance, strong correlations may exist between fish and beef(due to being in same sector), but may no exist between wheat and rice . Metals like aluminum and zinc often move together, influenced by industrial demand cycles.

2. **Heatmap 2 – Filtered Correlations (> 0.8):**
                
To focus on the most significant relationships, we created a second heatmap that only includes correlations above 0.8. This visualization isolates the strongest inter-commodity connections, allowing us to pinpoint key pairs for deeper regression study.
From this, we observe that several commodities share very high correlation scores, often across different sectors — highlighting how global markets are not isolated but mutually responsive

The Boxes in the light(1) shows the correlation which is >0.83 between, a strong correlation.               
These heatmaps collectively demonstrate how macroeconomic forces synchronize price movements across otherwise unrelated commodities. By filtering for strong correlations, we identify the most meaningful pairs that can be modeled through linear regression to estimate predictive relationships and R² values.""")
    map1,map2= st.tabs(["H-map1","H-map2"])
    with map1:
        st.image("H-map1.png",clamp=True,width="stretch")
    with map2:
        st.image("H-map2.png")
    st.divider()

def show_algo():
    st.header(":blue[Regression Analysis]")
    st.subheader("The Algorithm")
    st.markdown("""Linear Regression is one of the most fundamental and widely used algorithms in statistical modeling and machine learning. It helps us understand the relationship between two quantitative variables — one acting as the independent variable (predictor) and the other as the dependent variable (response).

In simple terms, linear regression examines how changes in one variable can predict changes in another. The relationship is expressed through a straight-line equation, which fits the data in such a way that the difference between the predicted and actual values is minimized.

In this project, we used Simple Linear Regression to analyze the pairwise relationships between highly correlated commodities identified from our second heatmap. Out of 17 commodities, we filtered 11 pairs of commodities that showed correlation values above 0.8. These pairs represent the strongest linear relationships across different sectors — such as between energy and agriculture, metals and industry, or within similar commodity categories.
                
                """)
    st.subheader("Mathematical Representation")
    st.markdown("""The basic equation of a linear regression model is:
                
$$
Y= β_0 + β_1X + ϵ
$$
Where:
- $$Y →$$ Dependent variable (the value we want to predict)
- $$X →$$ Independent variable (the predictor)
- $$𝛽_0 →$$ Intercept term (value of Y when X = 0)
- $$β_1 →$$ Slope coefficient (the rate at which Y changes for each unit change in X)
- $$ϵ →$$ Random error term (difference between actual and predicted values)         

The goal of the algorithm is to determine the best-fitting line through the data points. This is done by minimizing the Sum of Squared Errors (SSE) between the actual and predicted values:
$$
SSE = \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2
$$       
where $$Y_i$$ is the actual value and $$\hat{Y}_i$$ is the predicted value from the regression line.

The smaller the SSE, the better the line fits the data.""")
    st.subheader("Understanding the R²")
    st.markdown("**How It Works in This Project**")
    st.markdown("""After plotting the correlation heatmaps, we identified 11 pairs of commodities with correlation values above 0.8. These pairs show strong positive linear relationships, meaning that as the price of one commodity increases, the other tends to increase as well.

We then applied Linear Regression analysis to these 11 relationships to test how accurately one commodity’s price can predict the other’s. For each pair, the independent variable (X) and dependent variable (Y) were selected, and the regression model was trained to find the best-fitting line through their data points.

The R² score (Coefficient of Determination) was calculated for each regression model to measure how well the model explains the variation in the dependent variable.""")
    st.markdown("")
    st.markdown("""The R² value is a statistical measure that represents the proportion of variance in the dependent variable that can be explained by the independent variable. It is given by:" \
    
$$
R^2=1-{SS_{res}}/{SS_{tot}}
$$ 
Where:
- $${SS_{res}}=\sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2$$(residual sum of squares)
                
- $${SS_{tot}}=\sum_{i=1}^{n} (Y_i - \overline{Y}_i)^2 $$(total sum of squares)

An R² value ranges between 0 and 1:

- $$R² = 1 →$$ Perfect fit (the model explains 100% of the data variance).

- $$R² = 0 →$$ No explanatory power (the model cannot explain any variation).

In the context of this project, the R² value tells us how strongly the prices of two commodities are related. A higher R² indicates that one commodity’s price can be reliably predicted from the other.""")

    st.markdown("While there’s no strict universal cutoff for a “good” R², the general interpretation in financial and commodity data analysis is:")
    R_df=pd.DataFrame({
        "R² Score": ["0.0 – 0.3","0.3 – 0.7"," greater than 0.7"],
        "Interpretation": ["Weak relationship","Moderate relationship","Strong relationship"]
    })
    st.table(R_df)
    st.markdown("""In this project, we consider R² > 0.7 as a strong indication that the commodities share a meaningful economic relationship. Such high scores imply that a significant portion of one commodity’s price variation can be predicted using another’s price trend.
                
For each of the 11 selected pairs, the regression model outputs:

- Slope (β₁): Indicates the rate at which Y changes per unit increase in X.

- Intercept (β₀): The base value of Y when X = 0.

- R² Score: Reflects the model’s predictive strength.

By comparing R² scores across all pairs, we can identify which relationships are most linear and predictable.""")
    st.subheader("R² Score Analysis")
    st.markdown(""" After performing the Linear Regression analysis on the 11 highly correlated commodity pairs (identified from the heatmap with correlation values above 0.8), we calculated the R² scores for each pair.
These R² values represent how much of the variation in one commodity’s price can be explained by another.

This step allows us to quantitatively assess the strength and reliability of the relationships between different commodities — spanning energy, agriculture, metals, and food sectors.""")
    data = {
    "Commodity Relationship": [
        "Crude Oil vs Soybean Oil",
        "Soybean Oil vs Wheat",
        "Soybean Oil vs Iron Ore",
        "Urea vs Soybean Oil",
        "Wheat vs Urea",
        "Zinc vs Aluminum",
        "Crude Oil vs Iron Ore",
        "Rubber vs Iron Ore",
        "Bananas vs Fish",
        "Beef vs Fish",
        "Beef vs Bananas"
    ],
    "R² Score": [0.66, 0.83, 0.75, 0.777, 0.69, 0.67, 0.73, 0.63, 0.71, 0.65, 0.71]
}
    df = pd.DataFrame(data)
    def label_strength(r2):
        if r2 >= 0.8:
            return "Strong"
        elif r2 >= 0.6:
            return "Moderate"
        else:
            return "Weak"
    df["Relationship Strength"] = df["R² Score"].apply(label_strength)
    st.subheader("R² Score of Commodity Relationships")
    df = (
    df.style
    .applymap(
        lambda _: "background-color: CornflowerBlue;", subset=([1], slice(None))
    )
    .format({'R² Score': '{:.3f}'})
    )
    st.dataframe(df)
    st.markdown("""The R² scores show a mix of strong and moderate relationships among the analyzed commodity pairs.
Here’s what the results reveal:

- **Strong Relationships (R² ≥ 0.7):**
These pairs exhibit a high level of dependency, meaning changes in one commodity can predict price variations in the other with considerable accuracy.
Examples include:

    1. Soybean Oil vs Wheat (0.83): Reflects a strong agricultural connection since both are crop-based commodities influenced by climate and global food demand.

    2. Urea vs Soybean Oil (0.78): Indicates how energy-linked agricultural inputs like fertilizers (urea) respond to prices of plant-based oils used in both food and biofuel industries.

    3. Crude Oil vs Iron Ore (0.73): Demonstrates industrial interlinkage — when industrial activity rises, both energy and metal demands surge.

    4. Bananas vs Fish (0.71) and Beef vs Bananas (0.71): Suggest that food commodities often follow broader consumption and logistics cost patterns.

- **Moderate Relationships (R² between 0.6 and 0.7):**
These relationships indicate partial predictability, where one commodity influences the other, but additional factors also play a role.
Examples:

    1. Crude Oil vs Soybean Oil (0.66): While energy impacts biofuel-linked agricultural oils, other factors like crop yield and weather also contribute.

    2. Zinc vs Aluminum (0.67): Industrial metals often move together, but varying production costs and supply chains cause moderate deviations.

    3. Beef vs Fish (0.65): Indicates moderate correlation due to shared market demand in protein consumption, but differing production cycles.

Overall, the R² values range from 0.63 to 0.83, showing that all selected pairs exhibit either moderate or strong relationships, with none classified as weak (<0.5).
This validates that the heatmap-based selection method effectively identified economically meaningful pairs.""")
    st.divider()

def show_results():
    st.subheader(":blue[Results]")
    st.markdown("""After obtaining the R² scores for all the identified relationships between different commodities, the next step involves visually representing these relationships through regression plots. Each regression plot combines two key components — a scatter plot showing the actual data points and a regression line that represents the model’s predicted trend. This visualization helps interpret the strength and direction of the relationship between two commodity prices in a much clearer and more intuitive way than raw numbers alone.

In this section, we will plot the regression results for each commodity pair, showing how closely one commodity’s price follows the pattern of another. The line in each graph represents the best fit produced by the linear regression model, while the individual dots (scatter points) represent the real data observations. By analyzing these plots, we can validate whether the statistical R² values we calculated earlier truly correspond to the observed patterns in the dataset.""")
    st.subheader("*Regression Graph of Strong relationship*")
    
    s1,s2,s3,s4,s5,s6= st.tabs(["1","2","3","4","5","6"])
    with s1:
        st.subheader("Soybean Oil price vs Wheat Price")
        st.image('s1.png')
    with s2:
        st.subheader("Soybean Oil vs Iro Ore")
        st.image('s2.png')
    with s3:
        st.subheader("Urea vs Soybean oil")
        st.image('s3.png')
    with s4:
        st.subheader("Crude Oil vs Iron Ore")
        st.image('s4.png')
    with s5:
        st.subheader("Bannas vs Fish")
        st.image('s5.png')
    with s6:
        st.subheader("Beef vs Bannana")
        st.image('s6.png')
    st.markdown("")
    st.subheader("*Regression Graph of Moderate relationship*")
    m1,m2,m3,m4,m5= st.tabs(["1","2","3","4","5"])
    with m1:
        st.subheader("Crude Oil vs Soybean Oil price")
        st.image('w1.png')
    with m2:
        st.subheader("Wheat Price vs Urea Price")
        st.image('w2.png')
    with m3:
        st.subheader("Zinc vs Aluminum")
        st.image('w3.png')
    with m4:
        st.subheader("Rubber vs Iron Ore")
        st.image('w4.png')
    with m5:
        st.subheader("Beef vs Fish")
        st.image('w5.png')

    st.divider()
    st.subheader(":blue[Conclusion]")
    st.markdown("""After performing both the correlation analysis and linear regression modeling, several meaningful patterns emerged among the 17 global commodities studied. While the heatmap initially gave a broad view of which commodities move together, the regression analysis provided a more detailed understanding of how strongly one commodity’s price can predict another’s.

#### 1. Weak or Negligible Relationships

From the heatmap and regression plots, it is evident that commodities such as Sugar, Rice, Chicken, Coconut Oil, Cotton, and Plywood exhibit very weak or no significant linear correlation with other commodities. Their prices fluctuate largely due to sector-specific factors such as agricultural yields, regional weather conditions, domestic demand, and local policy changes rather than global commodity price trends.
These items, particularly food staples like rice and sugar, are heavily influenced by country-level agricultural and trade policies, making them relatively insulated from industrial commodities or energy market trends. In the regression plots, their scatter points were widely spread with no clear linear pattern, indicating low R² scores and poor predictive relationships with other variables.

#### 2. Moderate Relationships — Industrial and Energy Sectors

A large portion of the studied commodities fall into the moderate correlation range, with R² values between 0.6 and 0.75. Examples include:

Crude Oil vs Iron Ore (0.73)

Zinc vs Aluminum (0.67)

Bananas vs Fish (0.71)

Beef vs Bananas (0.71)

Beef vs Fish (0.65)

These results make practical sense because energy and industrial metals are interlinked through production and transportation costs. Similarly, agricultural and livestock commodities share indirect dependencies, especially in terms of feed prices and market demand. The regression plots for these pairs showed fairly tight clusters of points following the regression line, confirming consistent linear trends but with some natural dispersion due to market variability.

#### 3. Strong Relationships — Fertilizer and Agricultural Commodities

The strongest relationships were observed in pairs like:

Soybean Oil vs Wheat (R² = 0.83)

Urea vs Soybean Oil (R² = 0.78)

These high R² values suggest a strong predictive relationship between these commodities. Soybean Oil, being a key agricultural output, is heavily tied to crop markets, while Urea is an essential fertilizer influencing agricultural yields. The regression lines for these pairs showed clear upward trends with points closely following the fitted line, confirming that price variations in one can be used to reliably forecast the other.
Such strong correlations highlight the interconnectedness between the agricultural and chemical fertilizer sectors, reflecting how changes in one market often directly impact another.

#### 4. Sector-Specific Exceptions

Interestingly, Rubber displayed a selective correlation pattern. It forms a moderately strong relationship with Iron Ore (R² = 0.63) but weak correlations elsewhere. This could be attributed to shared industrial usage — both are heavily tied to the manufacturing and automotive industries — yet they respond differently to raw material demand fluctuations.

On the other hand, Soybean Oil emerges as a key connecting commodity across multiple sectors, showing good correlations not only with agricultural commodities like wheat and urea but also moderate ones with metals such as iron ore. This suggests that soybean oil prices may serve as a cross-sector indicator, reflecting broader economic and market trends.

#### 5. General Trend

Overall, the regression analysis confirms that not all commodities move together; rather, specific groups within agriculture, energy, and metals show stronger internal coherence. Commodities like sugar, rice, chicken, and plywood behave more independently, while core industrial and agricultural commodities reveal structured relationships with clear predictive potential.
The regression plots thus serve as visual proof of the interconnected nature of global trade sectors — where some commodities respond together under shared economic conditions, while others are governed by localized and independent market forces.
""")
    st.divider()
    st.subheader(":blue[Limitations]")
    st.markdown("""While the present project provides valuable insights into the relationships between commodities from various sectors using linear regression and correlation analysis, it is essential to acknowledge its methodological and analytical limitations. These constraints define the scope of interpretation and help in identifying areas for future improvement and model enhancement.

##### 1. Reliance on Simple Linear Regression

The most significant limitation of this study is that it relies solely on the simple linear regression model. Although linear regression provides an effective first step for identifying potential relationships, it assumes a strictly linear dependency between two variables. In real-world economic systems, commodity prices are influenced by multiple interacting factors that often display non-linear, cyclical, or seasonal behaviors. Hence, the simple model may oversimplify complex market dynamics, failing to capture hidden trends or lagged effects that a multi-variable or non-linear model could reveal.

##### 2. Consideration of Only Price Factor

The analysis is based entirely on the price values of commodities, without including other influential economic indicators such as demand, supply volume, inflation rate, production cost, or global trade policies. Price is only one dimension of market behavior. Therefore, by considering only this single variable, the study overlooks other macroeconomic variables that might explain why certain commodities move together while others diverge. This simplification restricts the model’s ability to provide a deeper understanding of causal relationships.

##### 3. Lack of Sectoral Specificity

Although the commodities are drawn from diverse sectors — including energy, metals, and agriculture — the project does not attempt to derive sector-level correlation conclusions. For example, even though Soybean Oil and Wheat show a strong relationship, this does not necessarily mean that all agricultural commodities correlate similarly. The findings are therefore pair-specific and cannot be generalized to entire sectors or industries. This limits the broader interpretability of cross-sectoral relationships.

##### 4. Absence of Temporal Dynamics

One of the most critical limitations is the exclusion of the time factor in the analysis. Commodity prices are inherently time-dependent and exhibit trends, cycles, and seasonality. The current model compares prices across commodities without accounting for temporal progression — meaning that the regression only examines static relationships between pairs, not how they evolve over time. Since most commodities have increased in price over the years due to inflation, technological development, or resource scarcity, ignoring time introduces bias and can lead to spurious correlations.

##### 5. Simplified Interpretation and Limited Predictive Power

Because the analysis is purely statistical and does not incorporate domain-specific or causal modeling, it cannot be used to draw policy conclusions or make economic forecasts. The results primarily describe correlations, not causations. Furthermore, since no external validation or out-of-sample testing was performed, the model’s predictive strength remains unverified.

##### 6. Data Scope and External Factors

The study uses historical monthly price data, but global market conditions can shift rapidly due to political instability, supply chain disruptions, or environmental events. Such shocks cannot be captured by a static linear model. Hence, the insights presented should be viewed as indicative rather than definitive.
""")
    st.divider()

def show_references():
    st.header(":blue[References/Data Sources]")
    st.markdown("""

#### 1. Data Sources:

- Macrotrends – Historical monthly commodity prices and rupee exchange rate data were primarily collected from https://www.macrotrends.net
.

- World Bank Commodity Prices (The Pink Sheet) – Used as a secondary source for verifying global commodity price trends: https://www.worldbank.org/en/research/commodity-markets
.

- Index Mundi – Additional commodity price data, especially for agricultural and energy sectors, were referenced from https://www.indexmundi.com/
.

- Rupee Exchange Rate Data – To account for currency effects (as most commodity prices are USD-based), historical INR/USD rates were taken from https://www.macrotrends.net/2551/rupee-dollar-exchange-rate-historical-chart
.

#### 2. Libraries and Tools Used:

- Python 3.x – Core programming language.

- Streamlit – For developing the interactive data visualization app.

- Pandas – For organizing and cleaning the dataset.

- Matplotlib / Seaborn – For correlation heat maps and regression visualization.

- Scikit-learn (sklearn) – For implementing linear regression models and calculating R² values.

#### 3. References and Support:

- ChatGPT (OpenAI, 2025) – Used to assist in writing theoretical explanations, algorithm details, and structuring project documentation.

- Official Python Documentation – https://docs.python.org/

- Scikit-learn Documentation – https://scikit-learn.org/stable/

- Streamlit Documentation – https://docs.streamlit.io/

#### 4. Additional Reading:
                
- Kirikkaleli, Dervis, and Hasan Güngör. (2021). Co-movement of commodity price indexes and energy price index: A wavelet coherence approach. Financial Innovation, 7(1), 1–18.
https://jfin-swufe.springeropen.com/articles/10.1186/s40854-021-00230-8

""")
    st.divider()
    st.subheader("Connect")
    st.markdown("""
- GitHub @Hercules-078
                
- Twitter @Hercules-078
                
- LinkdIn @hercules078
                
                """)

def show_all_sections():
    show_abstract()
    show_methodology()
    show_algo()
    show_results()
    show_references()

page = st.sidebar.radio("",["All section","Abstract","Methodology","Algorithm","Conclusion","References/Data Sources"])

if page == "All section":
    show_all_sections()
elif page == "Abstract":
    show_abstract()
elif page == "Methodology":
    show_methodology()
elif page == "Algorithm":
    show_algo()
elif page == "Conclusion":
    show_results()
elif page == "References/Data Sources":
    show_references()


