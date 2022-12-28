def load_apple_example() -> str:
    example_text = '''Apple Inc. is an American multinational technology company that specializes in consumer electronics, software and online services headquartered in Cupertino, California, United States. Apple is the largest information technology company by revenue (totaling US$365.8 billion in 2021) and as of May 2022, it is the world's second-most valuable company,[7] the fourth-largest personal computer vendor by unit sales and second-largest mobile phone manufacturer. It is one of the Big Five American information technology companies, alongside Alphabet, Amazon, Meta, and Microsoft.

Apple was founded as Apple Computer Company on April 1, 1976, by Steve Jobs, Steve Wozniak and Ronald Wayne to develop and sell Wozniak's Apple I personal computer. It was incorporated by Jobs and Wozniak as Apple Computer, Inc. in 1977 and the company's next computer, the Apple II became a best seller. Apple went public in 1980, to instant financial success. The company developed computers featuring innovative graphical user interfaces, including the original Macintosh, announced in a critically acclaimed advertisement, "1984", directed by Ridley Scott. By 1985, the high cost of its products and power struggles between executives caused problems. Wozniak stepped back from Apple amicably, while Jobs resigned to found NeXT, taking some Apple employees with him.'''
    
    example_question = '''Who started this company?'''
    
    return example_text, example_question

def load_tesla_example() -> str:
    example_text = '''Overview

We design, develop, manufacture, sell and lease high-performance fully electric vehicles and energy generation and storage systems, and offer services related to our sustainable energy products. We generally sell our products directly to customers, including through our website and retail locations. We also continue to grow our customer-facing infrastructure through a global network of vehicle service centers, Mobile Service technicians, body shops, Supercharger stations and Destination Chargers to accelerate the widespread adoption of our products. We emphasize performance, attractive styling and the safety of our users and workforce in the design and manufacture of our products and are continuing to develop full self-driving technology for improved safety. We also strive to lower the cost of ownership for our customers through continuous efforts to reduce manufacturing costs and by offering financial services tailored to our products. Our mission to accelerate the world’s transition to sustainable energy, engineering expertise, vertically integrated business model and focus on user experience differentiate us from other companies.

Segment Information

We operate as two reportable segments: (i) automotive and (ii) energy generation and storage.

The automotive segment includes the design, development, manufacturing, sales and leasing of electric vehicles as well as sales of automotive regulatory credits. Additionally, the automotive segment is also comprised of services and other, which includes non-warranty after-sales vehicle services, sales of used vehicles, retail merchandise, sales by our acquired subsidiaries to third party customers and vehicle insurance revenue. The energy generation and storage segment includes the design, manufacture, installation, sales and leasing of solar energy generation and energy storage products and related services and sales of solar energy systems incentives.'''
    
    example_question ='''What is this company's goal?'''
    
    return example_text, example_question

def load_apple_example_sentiment_analysis() -> str:
    example_text = '''Apple today announced financial results for its fiscal 2022 second quarter ended March 26, 2022. The Company posted a March quarter revenue record of $97.3 billion, up 9 percent year over year, and quarterly earnings per diluted share of $1.52.
“This quarter’s record results are a testament to Apple’s relentless focus on innovation and our ability to create the best products and services in the world,” said Tim Cook, Apple’s CEO. “We are delighted to see the strong customer response to our new products, as well as the progress we’re making to become carbon neutral across our supply chain and our products by 2030. We are committed, as ever, to being a force for good in the world — both in what we create and what we leave behind.”
“We are very pleased with our record business results for the March quarter, as we set an all-time revenue record for Services and March quarter revenue records for iPhone, Mac, and Wearables, Home and Accessories. Continued strong customer demand for our products helped us achieve an all-time high for our installed base of active devices,” said Luca Maestri, Apple’s CFO. “Our strong operating performance generated over $28 billion in operating cash flow, and allowed us to return nearly $27 billion to our shareholders during the quarter.”'''

    return example_text

def load_tesla_example_sentiment_analysis() -> str:
    example_text = '''We may be impacted by macroeconomic conditions resulting from the global COVID-19 pandemic.

Since the first quarter of 2020, there has been a worldwide impact from the COVID-19 pandemic. Government regulations and shifting social behaviors have limited or closed non-essential transportation, government functions, business activities and person-to-person interactions. In some cases, the relaxation of such trends has been followed by actual or contemplated returns to stringent restrictions on gatherings or commerce, including in parts of the U.S., and the rest of the world. 

During 2020, we temporarily suspended operations at each of our manufacturing facilities worldwide, and certain of our suppliers also shut down operations temporarily or permanently, including during the recently re-imposed lockdowns in certain parts of the world. We instituted temporary employee furloughs and compensation reductions while our U.S. operations were scaled back. Temporary impediments to administrative activities supporting our operations also hampered our product deliveries and deployments. 

Global trade conditions and consumer trends that originated during the pandemic continue to persist and may also have long-lasting adverse impact on us and our industries independently of the progress of the pandemic. For example, pandemic-related issues have exacerbated port congestion and intermittent supplier shutdowns and delays, resulting in additional expenses to expedite delivery of critical parts. Similarly, increased demand for personal electronics has created a shortfall of semiconductors, which has caused challenges in our supply chain and production. In addition, labor shortages resulting from the pandemic, including worker absenteeism, may lead to increased difficulty in hiring and retaining manufacturing and service workers, as well as increased labor costs. Sustaining our production trajectory will require the ongoing readiness and solvency of our suppliers and vendors, a stable and motivated production workforce and government cooperation, including for travel and visa allowances. The contingencies inherent in the construction of, and ramp at, new facilities such as Gigafactory Berlin and Gigafactory Texas may be exacerbated by these challenges.

We cannot predict the duration or direction of current global trends or their sustained impact. Ultimately, we continue to monitor macroeconomic conditions to remain flexible and to optimize and evolve our business as appropriate, and we will have to accurately project demand and infrastructure requirements globally and deploy our production, workforce and other resources accordingly. If we experience unfavorable global market conditions, or if we cannot or do not maintain operations at a scope that is commensurate with such conditions or are later required to or choose to suspend such operations again, our business, prospects, financial condition and operating results may be harmed.'''
        
    return example_text

def load_tesla_example_ner() -> str:
    example_text = '''The Board of Directors serves as a prudent fiduciary for shareholders and oversees the management of Tesla’s business — including reviewing the effectiveness of Tesla’s Impact priorities, initiatives and programs and this report. With those responsibilities in mind, the Board sets high standards for Tesla and its employees, officers and directors; and we periodically add new, highly qualified independent directors to the Board, such as Larry Ellison and Kathleen Wilson-Thompson in 2018 and Hiromichi Mizuno in 2020. Implicit in this approach is the importance of sound corporate governance.'''

    return example_text

def load_apple_finance() -> str:
    example_text = '''Apple today announced financial results for its fiscal 2022 fourth quarter ended September 24, 2022. The Company posted a September quarter record revenue of $90.1 billion, up 8 percent year over year, and quarterly earnings per diluted share of $1.29, up 4 percent year over year. Annual revenue was $394.3 billion, up 8 percent year over year, and annual earnings per diluted share were $6.11, up 9 percent year over year.
“This quarter’s results reflect Apple’s commitment to our customers, to the pursuit of innovation, and to leaving the world better than we found it,” said Tim Cook, Apple’s CEO. “As we head into the holiday season with our most powerful lineup ever, we are leading with our values in every action we take and every decision we make. We are deeply committed to protecting the environment, to securing user privacy, to strengthening accessibility, and to creating products and services that can unlock humanity’s full creative potential.”'''

    example_categories = '''finance, sports'''
    
    return example_text, example_categories

def load_world_cup_sports() -> str:
    example_text = '''Lionel Messi, wearing a black Qatari robe over his blue-and-white Argentina shirt, kissed the World Cup, shuffled toward his teammates and hoisted the golden trophy high in the air.

It was an iconic sight that finally — definitively — places the soccer superstar in the pantheon of the game’s greatest players.

Messi’s once-in-a-generation career is complete: He is a World Cup champion.

In probably the wildest final in the tournament’s 92-year history, Argentina won its third World Cup title by beating France 4-2 in a penalty shootout after a 3-3 draw featuring two goals from the 35-year-old Messi and a hat trick by his heir apparent, France forward Kylian Mbappé.

“It’s just crazy that it became a reality this way,” Messi said. “I craved for this so much. I knew God would bring this gift to me. I had the feeling that this (World Cup) was the one.”'''

    example_categories = '''finance, sports'''
    
    return example_text, example_categories