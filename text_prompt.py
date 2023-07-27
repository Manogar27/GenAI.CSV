import openai
import os


openai.api_key  = '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'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

text = """
GHG emissions targets
In parallel with our intensity targets, we are
aiming to reduce our net annual Scope 1 and
Scope 2 GHG emissions from both the upstream
and downstream businesses by 52 MMtCO2
e
from our business as usual 2035 forecast emissions.
By 2035, consistent with the corporate growth
strategy in oil and gas production and
development of new businesses, particularly
hydrogen and liquids-to-chemicals, we forecast
our business as usual Scope 1 and Scope 2 GHG
emissions for our wholly-owned operated assets
will increase to 119 MMtCO2
e. Our goal is to
mitigate this growth in emissions and reduce
our emissions to 67 MMtCO2
e by 2035.
Targeted GHG reduction
Our Yanbu’ Refinery facility successfully
obtained the International Sustainability and
Carbon Certification under its circular cracker
oil initiative. The initiative drives the
certification relates to an in-house sustainable
circular route to produce circular cracker oil
from waste oil to reduce our Scope 2 GHG
carbon footprint.
What are we doing?
During 2022, we have made progress toward
achieving our 2035 and 2050 ambitions across
our five identified levers: energy efficiency,
reduced methane and flaring; increased
renewables; CCS; and offsets to address
emissions we cannot reduce or capture. For more
information on our 2022 efforts and impact,
please refer to pages 26 and 27.
We have also been conducting site-level
bottom-up assessments of what it would take
to decarbonize our assets. Once this is completed
in 2023, we will update our decarbonization
strategy in the next report.
GHG emissions
The Company’s GHG emissions management
program monitors direct (Scope 1) and indirect
(Scope 2) emissions from wholly-owned operated
assets, in a manner consistent with the GHG
Protocol. Despite increased hydrocarbon
production by 10% in 2022, total emissions
(Scope 1 emissions and Scope 2 emissions) from
the Company and its operationally controlled
entities increased by only 6% (71.8 MMtCO2
e
in 2022 versus 67.8 MMtCO2
e in 2021) compared
to the previous year.
This was enabled by more efficient operations
and a reduction in flaring intensity by 17%
compared to the previous year due to improved
operations of the Company’s in-house flare gas
recovery systems across several facilities. For
more information on our flaring, please refer
to page 28.
Digital twins
Our EXPEC Computer Center developed
a solution to reduce energy intensity and
emissions associated with operating subsurface
artificial lift systems, leveraging digital twin
technology by optimizing the performance
of our electric submersible pumps (ESP).
The system was trial tested across 42 ESP lifted
wells resulting in a 22% average reduction in
power consumption, equivalent to 12 GWh
of energy savings during 2022. It is projected
that deploying this solution across all fields will
result in a 25% average reduction in artificial
lift energy intensity at Company level.
What are we doing?
Scope 1 and Scope 2
emissions upstream
intensity: 15%
reduction by 2035
(kg CO2
e/boe)
-15%
10.21
8.7
2018
2035
-15%
Scope 1 and Scope 2
emissions GHG reduction
targeted by 2035
(MMtCO2
e)
119
52
67
2035
2035
722 2022
-52
Forecast
business-asusual growth
Targeted
GHG
reduction
Our Southern Area
Oil Operations
won a 2022 Society
of Petroleum
Engineers Regional
Distinguished
Corporate Support
Award for reducing
its emissions by
 600,000
tCO2
e
1. 2018 was the first year our GHG inventory was independently assured.
2. This figure has undergone external limited assurance in accordance to the ISAE 3000 (revised). The assurance report can be found online here.
Aramco Sustainability Report 2022
24
Differentiate Sustain Diversify Enable
1. This figure has undergone external limited assurance in accordance to the ISAE 3000 (revised). The assurance report can be found online here.
2. The Jazan Refinery (our downstream refinery) is excluded from our current GHG reporting because in 2022, it remains in the startup and stabilization phase and is not fully
operational. Aramco is working to stabilize the refinery’s operations and complete all necessary reporting configurations before the end of 2023. Reporting on the refinery’s
environmental and sustainability elements will commence immediately thereafter, in line with the Company’s commitment to operational transparency.
3. Fadhili Gas Plant is excluded from 2020 GHG emissions inventory.
4. These emission reductions were calculated from real vessel performance data at different speeds and application of the International Maritime Organization guidelines. Prior to
implementation, terminals benchmarked the initiative with other worldwide ports, such as Los Angeles and San Diego in the United States, and other countries including Canada
and Singapore.
Scope 1 emissions
(MMtCO2
e)
55.7
55.71,2
2020
2021
2022
52.31,2
50.21,2,3
Scope 2 emissions
(MMtCO2
e)
16.1
16.11,2
2020
2021
2022
15.5
18.1
1,2
1,2,3
Upstream carbon intensity
(kg CO2
e/boe)
10.3
10.31
2020
2021
2022
10.71
10.63
Upstream carbon intensity
The Company’s 2022 upstream carbon intensity
figure remains among the lowest in the industry
at 10.31 kg CO2
e/boe (2021: 10.71
 kg CO2
e/boe).
This improvement is predominantly driven by
energy efficiency, and reduced flaring across
Upstream operations due to improved reliability
and performance of our flare gas recovery
systems (FGRS). In 2022, two new FGRS became
operational in both Abu Ali and Qatif central
processing facility resulting in estimated annual
flared gas recovery of over 1.0 bscf per year.
Aramco is leveraging its R&D and technology
initiatives to develop, and implement innovative
approaches that could help lower emissions
across our industry and have potential
application in other industries.
For more details on what we have done during
2022 regarding our progress on our five levers
to meet our 2035 interim GHG targets, please
refer to pages 26-27.
Scope 3 — value chain emissions
Our focus is on measurement, reporting, and
management of those emissions within our direct
control. To date, we have not reported Scope 3
emissions from our supply chain or from
customers’ use of our products. We are working
on supporting the global energy transition towards
a lower carbon emissions future through investing
in technologies and working with suppliers to
integrate ESG performance measures through
our iktva program.
Vessel Speed Program
To support the national and corporate GHG reduction aspirations, our
terminals instituted the Vessel Speed Program reducing the speed of
vessels sailing through the Ras Tanura and Ju’aymah Port to 12 knots
from 15 knots. 12 knots was determined as the optimal speed based
on vessel engine efficiency, while minimizing impact on customers’
satisfaction or our reliability. It is estimated that the program has reduced
the GHG emissions of visiting ships by more than 90,000 tCO2
e per year4
.
What are we doing?
Our investment in hydrogen, chemicals and
renewable energy sources and the increasing share
of gas in our production provide products that
will support the global energy transition towards
a lower carbon emissions future. We continue
to invest in a number of product stewardship
partnerships and technologies to reduce emissions,
this includes research and development into low
emissions transport solutions.
During 2022, we increased our R&D spend
on developing potential solutions that will assist
the global energy transition towards a lower
carbon emissions future — notably over a 45%
increase in sustainable mobility R&D spend and
over 380% increase in crude to chemicals R&D
spend, reflecting the increasing importance of
these areas to our future business. For more
details on our R&D spend, please refer to
pages 40-41.
"""
prompt = f"""
take up the numerical value from the report,
need a summary report, 
which is delimited with triple backticks?

Review text: '''{text}'''
"""
response = get_completion(prompt)
print(response)