# To crawl a JavaScript-heavy site like `ubishops.ca` that requires rendering dynamic content, we'll combine **Scrapy** for crawling and **Selenium** for JavaScript rendering. Here's how to do it:
#
# ---
#
# ### **1. Setup Dependencies**
# Install required packages:
# ```bash
# pip install scrapy selenium webdriver-manager
# ```
#
# ---

### **2. Modified Spider with Selenium (ubishops_spider.py)**
# ```python
import scrapy
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urljoin

class UbishopsSpider(scrapy.Spider):
    name = 'ubishops_crawler'
    allowed_domains = ['ubishops.ca']
    start_urls = ['https://www.ubishops.ca/']

    custom_settings = {
        'DEPTH_LIMIT': 2,
        'CLOSESPIDER_PAGECOUNT': 20,
        'FEED_FORMAT': 'json',
        'FEED_URI': 'ubishops_links.json'
    }

    def __init__(self, *args, **kwargs):
        super(UbishopsSpider, self).__init__(*args, **kwargs)
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in background
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            options=chrome_options
        )

    def closed(self, reason):
        self.driver.quit()  # Close browser when done

    def parse(self, response):
        self.driver.get(response.url)
        rendered_body = self.driver.page_source
        links = self.driver.find_elements(By.TAG_NAME, 'a')

        # Extract all links
        extracted_links = []
        for link in links:
            href = link.get_attribute('href')
            if href and href.startswith('https://www.ubishops.ca/'):
                extracted_links.append(href)

        # Yield current page data
        yield {
            'url': response.url,
            'links': extracted_links,
        }

        # Follow links recursively
        for link in extracted_links:
            yield scrapy.Request(
                url=link,
                callback=self.parse,
                meta={'depth': response.meta.get('depth', 0) + 1}
            )
# ```
#
# ---

### **Key Modifications**
# 1. **Selenium Integration**:
# - Uses headless Chrome to render JavaScript.
# - `webdriver-manager` automatically handles ChromeDriver installation.
# - Rendered page source is extracted with `driver.page_source`.
#
# 2. **Link Extraction**:
# - Uses Selenium's `find_elements` to get all `<a>` tags.
# - Validates links to stay within `ubishops.ca`.
#
# 3. **Crawl Limits**:
# - `DEPTH_LIMIT` and `CLOSESPIDER_PAGECOUNT` prevent infinite crawling.
#
# ---

### **3. Run the Crawler**
# ```bash
# scrapy runspider ubishops_spider.py
# ```
#
# ---
#
# ### **4. Output**
# - Results are saved to `ubishops_links.json`.
# - Example entry:
# ```json

# ```
#
# ---
#
# ### **Notes**
# 1. **Dynamic Content Handling**:
# - For pages that load content lazily (e.g., via AJAX), add explicit waits:
# ```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for specific element to load
WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'dynamic-content'))
)
# ```
#
# 2. **Performance**:
# - Headless mode (`--headless`) speeds up rendering.
# - Avoid crawling too aggressively to prevent IP blocking.
#
# 3. **Alternatives**:
# - For complex sites, use `scrapy-selenium` middleware (more advanced setup).
#
# This approach ensures JavaScript-rendered pages are crawled effectively while maintaining Scrapy's scalability.

#
# Let’s proceed with the remaining tasks using the crawled data from `ubishops.ca`. We’ll cover **graph construction**, **PageRank implementation**, **sensitivity analysis**, and **edge-case handling** tailored to the crawled dataset.
#
# ---
#
# ### **1. Graph Construction (Updated for ubishops.ca Data)**
# **Code** (`graph_pagerank.py`):
# ```python
import json
import networkx as nx

def build_ubishops_graph(crawled_data_path):
    G = nx.DiGraph()
    allowed_domain = "ubishops.ca"

    with open(crawled_data_path, 'r') as f:
        for line in f:
            entry = json.loads(line)
            source = entry['url']
            G.add_node(source)

            for target in entry['links']:
                # Ensure links stay within ubishops.ca
                if allowed_domain in target:
                    G.add_edge(source, target)

    print(f"Graph stats: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    return G

# Example usage:
G = build_ubishops_graph('ubishops_links.json')
# ```
#
# **Key Features**:
# - Filters links to include only those within `ubishops.ca`.
# - Logs graph size for transparency.
#
# ---
#
# ### **2. PageRank Implementation (Handling Dangling Nodes)**
# **Code** (`pagerank.py`):
# ```python
def ubishops_pagerank(G, d=0.85, tol=1e-6, max_iter=100):
    nodes = list(G.nodes())
    N = len(nodes)
    if N == 0:
        return {}

    pr = {node: 1/N for node in nodes}

    for _ in range(max_iter):
        new_pr = {}
        dangling_sum = d * sum(pr[node] for node in nodes if G.out_degree(node) == 0) / N

        for node in nodes:
            # Contribution from inlinks
            inlink_contrib = sum(
                pr[predecessor] / G.out_degree(predecessor)
                for predecessor in G.predecessors(node)
            )
            # Update PageRank with damping and dangling nodes
            new_pr[node] = (1 - d)/N + d * inlink_contrib + dangling_sum

        # Check convergence
        delta = sum(abs(new_pr[node] - pr[node]) for node in nodes)
        if delta < tol:
            break
        pr = new_pr.copy()

    return pr

# Compute ranks for ubishops.ca graph
pr_scores = ubishops_pagerank(G, d=0.85)
```

# **Key Features**:
# - Explicitly handles dangling nodes by redistributing their rank using `dangling_sum`.
# - Uses the standard damping factor (`d=0.85`) to mitigate spider traps.
#
# ---
#
# ### **3. Sensitivity Analysis (Damping Factor Impact)**
# **Code** (`sensitivity_analysis.py`):
# ```python
import matplotlib.pyplot as plt

def analyze_ubishops_sensitivity(G):
    damping_factors = [0.5, 0.65, 0.85, 0.95]
    results = {}

    for d in damping_factors:
        pr = ubishops_pagerank(G, d=d)
        results[d] = pr

    # Compare top 5 pages across damping factors
    for d in damping_factors:
        sorted_pr = sorted(results[d].items(), key=lambda x: -x[1])
        print(f"\nTop pages (d={d}):")
        for rank, (url, score) in enumerate(sorted_pr[:5], 1):
            print(f"{rank}. {url}: {score:.5f}")

    # Plot rank stability for the homepage
    homepage = "https://www.ubishops.ca/"
    d_values = sorted(damping_factors)
    homepage_scores = [results[d].get(homepage, 0) for d in d_values]

    plt.figure(figsize=(10, 6))
    plt.plot(d_values, homepage_scores, marker='o', linestyle='-')
    plt.title(f"PageRank Sensitivity for {homepage}")
    plt.xlabel("Damping Factor (d)")
    plt.ylabel("PageRank Score")
    plt.grid(True)
    plt.show()

# Run analysis
analyze_ubishops_sensitivity(G)
# ```

# **Expected Output**:
# ```
# Top pages (d=0.85):
# 1. https://www.ubishops.ca/: 0.15234
# 2. https://www.ubishops.ca/admissions: 0.09821
# 3. https://www.ubishops.ca/academics: 0.07215
# ...
# ```
#
# ---

### **4. Handling Edge Cases**
#### **a. Dangling Nodes (Pages with No Outbound Links)**
# - Automatically handled by `dangling_sum`, which redistributes their rank proportionally to all nodes.

#### **b. Spider Traps (Cycles)**
# - The damping factor (`d=0.85`) ensures random jumps break cycles. For example:
# - If `d=0.85`, 15% of rank is redistributed randomly, preventing traps from absorbing all rank.
#
# #### **c. Disconnected Components**
# - Pages with no inlinks (e.g., isolated nodes) still receive rank via the `(1 - d)/N` term.
#
# ---
#
# ### **5. Validation Against NetworkX**
# To ensure correctness, compare your implementation with NetworkX’s built-in `pagerank`:
#     ```python
nx_pr = nx.pagerank(G, alpha=0.85)
print("NetworkX vs. Custom Implementation Correlation:",
      np.corrcoef(list(pr_scores.values()), list(nx_pr.values()))[0, 1])
# ```
#
# ---

### **6. How to Run**
# 1. **Crawl Data**:
# ```bash
# scrapy runspider ubishops_spider.py
# ```
# 2. **Build Graph & Compute PageRank**:
# ```bash
# python graph_pagerank.py
# ```
# 3. **Analyze Sensitivity**:
# ```bash
# python sensitivity_analysis.py
# ```
#
# ---

### **Key Observations from Sensitivity Analysis**
# 1. **Low Damping (`d=0.5`)**:
# - Rankings are more uniform due to frequent random jumps.
# - Less differentiation between important/unimportant pages.
#
# 2. **High Damping (`d=0.95`)**:
# - Rankings heavily depend on link structure.
# - May amplify biases (e.g., spider traps or overlinked pages).
#
# 3. **Standard Damping (`d=0.85`)**:
# - Balances random jumps and link-based authority.
# - Produces stable, intuitive rankings (e.g., homepage as most authoritative).
#
# ---

### **Documentation & Best Practices**
# - **Code Quality**:
# - Modular functions for crawling, graph building, and analysis.
# - Descriptive variable names (e.g., `dangling_sum`, `inlink_contrib`).
# - **Output**:
# - JSON data for reproducibility.
#     - Visualizations (e.g., sensitivity plots) for intuitive analysis.
#
# This end-to-end implementation addresses all project tasks while emphasizing practical challenges (JavaScript crawling, damping sensitivity) and theoretical concepts (dangling nodes, spider traps).