# Mini tutorials for use cases

The **Slash** project on GitHub is a web application designed to scrape popular e-commerce websites, helping users find the best deals quickly and efficiently. Here’s a mini-tutorial series to demonstrate typical use cases with practical examples:

### Quick Start
### **Goal**: Install Slash locally and configure the environment.

---

#### 1. Clone and Set Up Local Environment

1. **Clone the Repository**
First, ensure `git` is installed on your computer. Choose a desired location and run the following command to clone the GitHub repository:
    
    ```bash
    git clone <https://github.com/DFY-NCSU/slash-phase6.git>
    cd slash-phase6
    ```
    
2. **Set Up Python Environment and Install Dependencies**
This project uses Python 3. Make sure Python and `pip` are installed on your system. All required libraries are listed in the `requirements.txt` file, which can be installed with the following command:
    
    ```bash
    pip3 install -r requirements.txt
    ```
    
3. **Install PostgreSQL Database**
This project requires PostgreSQL for database support. If PostgreSQL is not installed, download and install the latest version from the [PostgreSQL official download page](https://www.postgresql.org/download/).
    

#### 2. Run the Project

1. **Navigate to the `src` Directory**
After installing all dependencies, move to the `src` folder:
    
    ```bash
    cd src
    
    ```
    
2. **Run the Main Program**
   - **For Mac**:
        
        ```bash
        python3 main.py
        
        ```
        
   While the main program is running, proceed with the steps below to start the Streamlit application.
    

#### 3. Launch the Streamlit Interface

Open a new terminal window, go up one directory level (`cd ..`), and then run the following command to start the user interface:

- **For Mac**:
    
    ```bash
    python3 -m streamlit run slash_user_interface.py
    ```
    

---

Following these steps should successfully set up and run the Slash application. If you have any questions or need further assistance, feel free to reach out.

---
### Use Case 1: Saving a Product to Favorites for Later Review
#### Scenario
A user is browsing for the best deal on noise-canceling headphones but wants to compare options across different platforms. They decide to save their preferred choices to the **Favorites** section for easy reference later.

#### Steps

1. **Search for Headphones**  
   The user enters "noise-canceling headphones" in the search bar and reviews the aggregated results from various e-commerce platforms.

2. **Identify Potential Products**  
   As the user scans through the options, they find two models they like, each available at different prices across different platforms.

3. **Add to Favorites**  
   The user clicks the **Favorite** button next to each selected product. The application saves these items to the **Favorites** list, storing essential details like the name, price, and platform source.

4. **Access the Favorites List**  
   The user navigates to the **Favorites** section, where they can quickly view all saved items, making it easier to compare their preferred choices in one place.

5. **Revisit Later for Purchase Decision**  
   The user returns to the application at a later time and goes directly to the **Favorites** list to review the saved products. They can compare prices, read reviews, and finally decide on the best purchase.

#### Benefits

- **Convenience**  
  The **Favorites** feature allows users to save products they are interested in, avoiding the need to search again later.

- **Organized Comparison**  
  By collecting products in the **Favorites** section, users can easily compare options without sifting through all search results.

- **Streamlined Shopping Experience**  
  Users can revisit the **Favorites** list at any time, which helps them make more informed and timely purchase decisions.


### Use Case 2: Running a Search Query
#### Goal
Retrieve deals for a specific item.

#### Steps

1. **Launch the Application**  
   Run the application, which will open a Streamlit interface in your web browser.

2. **Enter Search Criteria**  
   - In the search box, type the name of the item or brand you are looking for. 
   - For example, you could enter a general product category, such as `"laptop"`, or be more specific by entering a brand name like `"Dell"` or `"Apple"`.
   - This search box supports keywords, so you can refine your search by using terms like model names or specific attributes (e.g., `"gaming laptop"` or `"Dell XPS 13"`).

3. **Execute the Search**  
   - After entering the desired keywords, press **Enter** or click the **Search** button to start the query.
   - Slash will then start scraping data from supported e-commerce websites for the best deals that match your criteria.

4. **View Results**  
   - The application will display the search results in a structured format. Each result includes:
     - **Product Name**: The name of the product as listed on the e-commerce site.
     - **Price**: The listed price of the product.
     - **Platform**: The e-commerce website where the item was found.
     - **Link**: A direct link to the product page for further details or to make a purchase.
     - **Seller Rating (if available)**: The rating of the seller or item based on customer reviews.
   - Results are presented in JSON format for easy readability and structured viewing. Additionally, you can choose to view more details or follow links to the items on their respective platforms.

#### Summary

Using Slash's search query functionality allows you to efficiently gather and compare deals from multiple platforms, giving you the flexibility to filter and save your results for a streamlined shopping experience.

---

### Use Case 3: Filtering and Sorting Results

**Goal**: Narrow down deals by price, brand, or rating to quickly find the best match for your needs.

#### Steps

1. **Access Filters in the Streamlit UI**  
   - Once you have your initial search results, locate the filtering and sorting options in the Streamlit user interface.
   - These filters are designed to help you refine the results based on your specific criteria, such as price range, brand, or customer rating.

2. **Apply Price Filters**  
   - Use the **Price Range** filter to set minimum and maximum prices.
   - This option helps you exclude items that are too expensive or do not meet your budget requirements, allowing you to focus only on products within your target price range.

3. **Filter by Brand**  
   - If you prefer specific brands, use the **Brand** filter to select the names you want to prioritize in your results (e.g., `"Dell"`, `"Apple"`, `"Samsung"`).
   - This is particularly useful if you are loyal to a brand or looking for compatibility with other devices.

4. **Sort by Rating or Reviews**  
   - For quality assurance, use the **Customer Rating** filter to prioritize products with high ratings or positive reviews.
   - You can also sort by the **number of reviews** to focus on products with substantial customer feedback, which can be a good indicator of reliability.

5. **Sort by Price or Relevance**  
   - Choose the **Lowest Price** option to view the most affordable options first, making it easy to identify the best budget-friendly deal.
   - Alternatively, select **Relevance** to sort results based on how well they match your search query, ensuring you see the most accurate matches first.

6. **Custom Sorting Options**  
   - Some filters may allow you to combine sorting options, such as **Lowest Price + High Rating**, for a more tailored selection.
   - This multi-layered approach gives you even more control over your search results, helping you narrow down to items that meet multiple criteria.

7. **Clear Filters (if needed)**  
   - If you want to reset the filters, use the **Clear Filters** button. This will return the list to the original, unfiltered results.
   - Clearing filters can be helpful if you want to adjust your search and try different filtering combinations.

#### Summary

By utilizing the filtering and sorting options in Slash, you can effectively narrow down the search results to find products that meet your budget, brand preference, and quality standards, making it easier to make a well-informed purchase.
