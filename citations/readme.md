# Extracting Structured Citations from PDFs 

Using Grobid (https://github.com/kermitt2/grobid/)

#### Installing 

Requirements for OSX:

* Homebrew 
* Gradle

```
brew install gradle

# Latest rc
wget https://github.com/kermitt2/grobid/archive/0.5.0.zip

cd grobid-0.5.0/
./gradlew clean install
```

For web application go to: http://localhost:8070/

__Sample Document__: Burroughs.pdf

__Sample Output__: XML

```xml
<TEI
    xmlns="http://www.tei-c.org/ns/1.0"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:mml="http://www.w3.org/1998/Math/MathML">
    <teiHeader/>
    <text>
        <front/>
        <body/>
        <back>
            <div>
                <listBibl>
                    <biblStruct xml:id="b0">
                        <analytic>
                            <title level="a" type="main">Diel feeding chronology and diet selection of rainbow trout (Onchorynchus mykiss) in the Henry&apos;s Fork of the Snake River</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">T</forename>
                                    <forename type="middle">R</forename>
                                    <surname>Angradi</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">S</forename>
                                    <surname>Griffith</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Idaho. Canadian Journal of Fisheries and Aquatic Sciences</title>
                            <imprint>
                                <biblScope unit="volume">47</biblScope>
                                <biblScope unit="page" from="199" to="209" />
                                <date type="published" when="1990" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b1">
                        <analytic>
                            <title level="a" type="main">Streamflow regulation and fish community structure</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">M</forename>
                                    <forename type="middle">B</forename>
                                    <surname>Bain</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">T</forename>
                                    <surname>Finn</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">H</forename>
                                    <forename type="middle">E</forename>
                                    <surname>Booke</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Ecology</title>
                            <imprint>
                                <biblScope unit="volume">69</biblScope>
                                <biblScope unit="issue">2</biblScope>
                                <biblScope unit="page" from="382" to="392" />
                                <date type="published" when="1988" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b2">
                        <analytic>
                            <title level="a" type="main">A perspective on America&apos;s vanishing streams</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">A</forename>
                                    <forename type="middle">C</forename>
                                    <surname>Benke</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Journal of the North American Benthological Society</title>
                            <imprint>
                                <biblScope unit="volume">9</biblScope>
                                <biblScope unit="issue">1</biblScope>
                                <biblScope unit="page" from="77" to="88" />
                                <date type="published" when="1990" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b3">
                        <analytic>
                            <title level="a" type="main">Morphological features of small streams: significance and function</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">R</forename>
                                    <forename type="middle">L</forename>
                                    <surname>Beschta</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">W</forename>
                                    <forename type="middle">S</forename>
                                    <surname>Platts</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Water Resources Bulletin</title>
                            <imprint>
                                <biblScope unit="volume">22</biblScope>
                                <biblScope unit="page" from="369" to="79" />
                                <date type="published" when="1986" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b4">
                        <monogr>
                            <title level="m" type="main">Chapter 1 of &quot;The effects of dam removal on fluvial geomorphology and fish; a dissertation of the Department of Fisheries &amp; Wildlife</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">B</forename>
                                    <forename type="middle">A</forename>
                                    <surname>Burroughs</surname>
                                </persName>
                            </author>
                            <imprint>
                                <date type="published" when="2007" />
                                <publisher>Manistee Co</publisher>
                                <pubPlace>Michigan</pubPlace>
                            </imprint>
                            <respStmt>
                                <orgName>Michigan State University</orgName>
                            </respStmt>
                        </monogr>
                        <note>The effects of Stronach Dam removal on fluvial geomorphology of the Pine River</note>
                    </biblStruct>
                    <biblStruct xml:id="b5">
                        <monogr>
                            <title level="m" type="main">Chapter 2 of &quot;The effects of dam removal on fluvial geomorphology and fish; a dissertation of the Department of Fisheries &amp; Wildlife</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">B</forename>
                                    <forename type="middle">A</forename>
                                    <surname>Burroughs</surname>
                                </persName>
                            </author>
                            <imprint>
                                <date type="published" when="2007" />
                                <publisher>Manistee Co</publisher>
                                <pubPlace>Michigan</pubPlace>
                            </imprint>
                            <respStmt>
                                <orgName>Michigan State University</orgName>
                            </respStmt>
                        </monogr>
                        <note>The effects of Stronach Dam removal on fish in the Pine River</note>
                    </biblStruct>
                    <biblStruct xml:id="b6">
                        <analytic>
                            <title level="a" type="main">An integrative approach towards understanding ecological responses to dam removal: the Manatawny Creek study</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">K</forename>
                                    <forename type="middle">L</forename>
                                    <surname>Bushaw-Newton</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">D</forename>
                                    <forename type="middle">D</forename>
                                    <surname>Hart</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">E</forename>
                                    <surname>Pizzuto</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">R</forename>
                                    <surname>Thomson</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <surname>Egan</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">T</forename>
                                    <surname>Ashley</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">T</forename>
                                    <forename type="middle">E</forename>
                                    <surname>Johnson</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">R</forename>
                                    <forename type="middle">K</forename>
                                    <surname>Horwitz</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">M</forename>
                                    <surname>Keeley</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <surname>Lawrence</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">D</forename>
                                    <surname>Charles</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">C</forename>
                                    <surname>Gatenby</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">D</forename>
                                    <forename type="middle">A</forename>
                                    <surname>Kreeger</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">T</forename>
                                    <surname>Nightengale</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">R</forename>
                                    <forename type="middle">L</forename>
                                    <surname>Thomas</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">D</forename>
                                    <forename type="middle">J</forename>
                                    <surname>Velinsky</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Journal of the American Water Resources Association</title>
                            <imprint>
                                <biblScope unit="volume">38</biblScope>
                                <biblScope unit="issue">6</biblScope>
                                <biblScope unit="page" from="1581" to="1599" />
                                <date type="published" when="2002" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b7">
                        <analytic>
                            <title level="a" type="main">Framework for monitoring and preliminary results after removal of Good Hope Mill Dam</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">J</forename>
                                    <surname>Chaplin</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Economics and the Environment</title>
                            <editor>W.L. Graf editor. The H. John Heinz III Center for Science</editor>
                            <imprint>
                                <date type="published" when="2003" />
                            </imprint>
                        </monogr>
                        <note>Chapter 8 in; Dam removal research: status and prospects</note>
                    </biblStruct>
                    <biblStruct xml:id="b8">
                        <analytic>
                            <title level="a" type="main">Dams and rivers: primer on the downstream effects of dams</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">M</forename>
                                    <surname>Collier</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">R</forename>
                                    <forename type="middle">H</forename>
                                    <surname>Webb</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">C</forename>
                                    <surname>Schmidt</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">U.S. Geological Survey Circular</title>
                            <imprint>
                                <biblScope unit="volume">1126</biblScope>
                                <biblScope unit="page">p</biblScope>
                                <date type="published" when="1996" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b9">
                        <monogr>
                            <title level="m" type="main">An evaluation of some techniques for the collection and analysis of benthic samples with special emphasis on lotic waters</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">K</forename>
                                    <forename type="middle">W</forename>
                                    <surname>Cummins</surname>
                                </persName>
                            </author>
                            <imprint>
                                <date type="published" when="1962" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b10">
                        <analytic>
                            <title/>
                        </analytic>
                        <monogr>
                            <title level="j">American Midland Naturalist</title>
                            <imprint>
                                <biblScope unit="volume">67</biblScope>
                                <biblScope unit="page" from="477" to="504" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b11">
                        <analytic>
                            <title level="a" type="main">Review of ecological effects of rapidly varying flows downstream from hydroelectric facilities</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">R</forename>
                                    <forename type="middle">M</forename>
                                    <surname>Cushman</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">North American Journal of Fisheries Management</title>
                            <imprint>
                                <biblScope unit="volume">5</biblScope>
                                <biblScope unit="page" from="330" to="339" />
                                <date type="published" when="1985" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b12">
                        <analytic>
                            <title level="a" type="main">Predicting channel response to dam removal using geomorphic analogies</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">M</forename>
                                    <forename type="middle">W</forename>
                                    <surname>Doyle</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">E</forename>
                                    <forename type="middle">H</forename>
                                    <surname>Stanley</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">M</forename>
                                    <surname>Harbor</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Journal of American Water Resources Association</title>
                            <imprint>
                                <biblScope unit="volume">38</biblScope>
                                <biblScope unit="page" from="1567" to="1579" />
                                <date type="published" when="2002" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b13">
                        <analytic>
                            <title level="a" type="main">Stream ecosystem response to small dam removal: lessons from the heartland</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">M</forename>
                                    <forename type="middle">W</forename>
                                    <surname>Doyle</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Geomorphology</title>
                            <imprint>
                                <biblScope unit="volume">71</biblScope>
                                <biblScope unit="page" from="227" to="244" />
                                <date type="published" when="2005" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b14">
                        <analytic>
                            <title level="a" type="main">Lessons from a dam failure</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">E</forename>
                                    <surname>Evans</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">S</forename>
                                    <forename type="middle">D</forename>
                                    <surname>Mackey</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">F</forename>
                                    <surname>Gottgens</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">W</forename>
                                    <forename type="middle">M</forename>
                                    <surname>Gill</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Ohio Journal of Science</title>
                            <imprint>
                                <biblScope unit="volume">100</biblScope>
                                <biblScope unit="issue">5</biblScope>
                                <biblScope unit="page" from="121" to="131" />
                                <date type="published" when="2000" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b15">
                        <monogr>
                            <title level="m" type="main">Stream hydrology: an introduction for ecologists</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">N</forename>
                                    <forename type="middle">D</forename>
                                    <surname>Gordon</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">T</forename>
                                    <forename type="middle">A</forename>
                                    <surname>Mcmahon</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">B</forename>
                                    <forename type="middle">L</forename>
                                    <surname>Finlayson</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">C</forename>
                                    <forename type="middle">J</forename>
                                    <surname>Gippel</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">R</forename>
                                    <forename type="middle">J</forename>
                                    <surname>Nathan</surname>
                                </persName>
                            </author>
                            <imprint>
                                <date type="published" when="2004" />
                                <publisher>Wiley &amp; Sons Ltd. England</publisher>
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b16">
                        <analytic>
                            <title level="a" type="main">In press. Conservation considerations for small dams on coldwater streams</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">D</forename>
                                    <forename type="middle">B</forename>
                                    <surname>Hayes</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">H</forename>
                                    <forename type="middle">R</forename>
                                    <surname>Dodd</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">L</forename>
                                    <surname>Lessard</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="m">Proceedings of the 4th World Fisheries Congress</title>
                            <meeting>the 4th World Fisheries Congress
                                <address>
                                    <addrLine>Vancouver, BC</addrLine>
                                </address>
                            </meeting>
                            <imprint>
                                <date type="published" when="2004-05-26" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b17">
                        <analytic>
                            <title level="a" type="main">Seasonal changes in abundance of brown trout (Salmo trutta) and rainbow trout (S. gairdnerii) assessed by drift diving in the Rangitkei river</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">B</forename>
                                    <forename type="middle">J</forename>
                                    <surname>Hicks</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">N</forename>
                                    <forename type="middle">R N</forename>
                                    <surname>Watson</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">New Zealand Journal of Marine and Freshwater Research</title>
                            <imprint>
                                <biblScope unit="volume">19</biblScope>
                                <biblScope unit="page" from="1" to="10" />
                                <date type="published" when="1985" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b18">
                        <analytic>
                            <title level="a" type="main">Effects of dam removal on Dead Lake</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">M</forename>
                                    <forename type="middle">J</forename>
                                    <surname>Hill</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">E</forename>
                                    <forename type="middle">A</forename>
                                    <surname>Long</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">S</forename>
                                    <surname>Hardin</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="m">Proceedings of the Annual Conference SEAFWA</title>
                            <meeting>the Annual Conference SEAFWA
                                <address>
                                    <addrLine>Chipola River, Florida</addrLine>
                                </address>
                            </meeting>
                            <imprint>
                                <date type="published" when="1994" />
                                <biblScope unit="page" from="512" to="523" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b19">
                        <analytic>
                            <title level="a" type="main">Ecology of riverine fishes in regulated streams with emphasis on the Colorado River. Pages 57-74</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">P</forename>
                                    <forename type="middle">B</forename>
                                    <surname>Holden</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="m">Ecology of Regulated Streams</title>
                            <editor>J.V. Ward and J.A. Stanford</editor>
                            <meeting>
                                <address>
                                    <addrLine>New York</addrLine>
                                </address>
                            </meeting>
                            <imprint>
                                <publisher>Plenum Press</publisher>
                                <date type="published" when="1979" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b20">
                        <analytic>
                            <title level="a" type="main">Tales of the Undammed: removing barriers doesn&apos;t automatically restore river health</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">E</forename>
                                    <surname>Francisco</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Science News</title>
                            <imprint>
                                <biblScope unit="volume">165</biblScope>
                                <biblScope unit="issue">15</biblScope>
                                <date type="published" when="2004-04-10" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b21">
                        <analytic>
                            <title level="a" type="main">Changes in the habitat and fish community of the Milwaukee River, Wisconsin, following removal of the Woolen Mills Dam</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">P</forename>
                                    <surname>Kanehl</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">D</forename>
                                    <forename type="middle">J</forename>
                                    <surname>Lyons</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">E</forename>
                                    <surname>Nelson</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">North American Journal of Fisheries Management</title>
                            <imprint>
                                <biblScope unit="volume">17</biblScope>
                                <biblScope unit="page" from="387" to="400" />
                                <date type="published" when="1997" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b22">
                        <analytic>
                            <title level="a" type="main">The pebble count technique for quantifying surface bed material size in instream flow studies</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">D</forename>
                                    <surname>Knighton</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <surname>Arnold</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <surname>London</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">G</forename>
                                    <forename type="middle">M</forename>
                                    <surname>Kondolf</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">S</forename>
                                    <surname>Li</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">ASCE Proc</title>
                            <imprint>
                                <biblScope unit="volume">3</biblScope>
                                <biblScope unit="issue">2</biblScope>
                                <biblScope unit="page" from="80" to="87" />
                                <date type="published" when="1984" />
                            </imprint>
                        </monogr>
                        <note>Rivers</note>
                    </biblStruct>
                    <biblStruct xml:id="b23">
                        <analytic>
                            <title level="a" type="main">Effects of elevated water temperature on fish and macroinvertebrate communities below small dams</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">L</forename>
                                    <surname>Lessard</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">D</forename>
                                    <forename type="middle">B</forename>
                                    <surname>Hayes</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">River Research and Applications</title>
                            <imprint>
                                <biblScope unit="volume">19</biblScope>
                                <biblScope unit="page" from="721" to="732" />
                                <date type="published" when="2003" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b24">
                        <analytic>
                            <title level="a" type="main">Downstream ecological effects of dams</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">F</forename>
                                    <forename type="middle">K</forename>
                                    <surname>Ligon</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">W</forename>
                                    <forename type="middle">E</forename>
                                    <surname>Dietrich</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">W</forename>
                                    <forename type="middle">J</forename>
                                    <surname>Trush</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Bioscience</title>
                            <imprint>
                                <biblScope unit="volume">45</biblScope>
                                <biblScope unit="issue">3</biblScope>
                                <biblScope unit="page" from="183" to="192" />
                                <date type="published" when="1995" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b25">
                        <analytic>
                            <title level="a" type="main">Fish species composition before and after construction of a main stem reservoir on the White River</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">P</forename>
                                    <forename type="middle">J</forename>
                                    <surname>Martinez</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">T</forename>
                                    <forename type="middle">E</forename>
                                    <surname>Chart</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">M</forename>
                                    <forename type="middle">A</forename>
                                    <surname>Trammell</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">G</forename>
                                    <surname>Wullschleger</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">E</forename>
                                    <forename type="middle">P</forename>
                                    <surname>Bergersen</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Colorado. Environmental Biology of Fishes</title>
                            <imprint>
                                <biblScope unit="volume">40</biblScope>
                                <biblScope unit="page" from="227" to="239" />
                                <date type="published" when="1994" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b26">
                        <analytic>
                            <title level="a" type="main">Measuring of interspecific association and similarity between communities</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">M</forename>
                                    <surname>Morista</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Memoirs of the Faculty Science Kyushu University, Series E Biology</title>
                            <imprint>
                                <biblScope unit="volume">3</biblScope>
                                <biblScope unit="page" from="65" to="80" />
                                <date type="published" when="1959" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b27">
                        <analytic>
                            <title level="a" type="main">Long-term consequences of upstream impoundment</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">G</forename>
                                    <forename type="middle">E</forename>
                                    <surname>Petts</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Environmental Conservation</title>
                            <imprint>
                                <biblScope unit="volume">7</biblScope>
                                <biblScope unit="issue">4</biblScope>
                                <biblScope unit="page" from="325" to="332" />
                                <date type="published" when="1980" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b28">
                        <analytic>
                            <title level="a" type="main">Effects of dam removal on river form and process</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">G</forename>
                                    <forename type="middle">E</forename>
                                    <surname>Petts</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">I</forename>
                                    <surname>Foster</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <surname>Arnold</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <surname>London</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <surname>Pizzuto</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Bioscience</title>
                            <imprint>
                                <biblScope unit="volume">52</biblScope>
                                <biblScope unit="issue">8</biblScope>
                                <biblScope unit="page" from="683" to="691" />
                                <date type="published" when="1985" />
                            </imprint>
                        </monogr>
                        <note>Rivers and landscape</note>
                    </biblStruct>
                    <biblStruct xml:id="b29">
                        <analytic>
                            <title level="a" type="main">American dam removal census: available data and data needs</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">M</forename>
                                    <surname>Pohl</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Economics and the Environment</title>
                            <editor>W.L. Graf editor. The H. John Heinz III Center for Science</editor>
                            <imprint>
                                <date type="published" when="2003" />
                            </imprint>
                        </monogr>
                        <note>Chapter 2 in; Dam removal research: status and prospects</note>
                    </biblStruct>
                    <biblStruct xml:id="b30">
                        <analytic>
                            <title level="a" type="main">Regional effects of hydrologic alterations on riverine macrobiota in the New World: tropicaltemperate comparisons</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">C</forename>
                                    <forename type="middle">M</forename>
                                    <surname>Pringle</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">M</forename>
                                    <forename type="middle">C</forename>
                                    <surname>Freeman</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">B</forename>
                                    <forename type="middle">J</forename>
                                    <surname>Freeman</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Bioscience</title>
                            <imprint>
                                <biblScope unit="volume">50</biblScope>
                                <biblScope unit="issue">9</biblScope>
                                <biblScope unit="page" from="807" to="823" />
                                <date type="published" when="2000" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b31">
                        <analytic>
                            <title level="a" type="main">Fish assemblage changes in an Ozark river after impoundment: a long-term perspective</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">W</forename>
                                    <surname>Quinn</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">T</forename>
                                    <forename type="middle">J</forename>
                                    <surname>Kwak</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Transactions of the American Fisheries Society</title>
                            <imprint>
                                <biblScope unit="volume">132</biblScope>
                                <biblScope unit="page" from="110" to="119" />
                                <date type="published" when="2003" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b32">
                        <monogr>
                            <title level="m" type="main">The economy of nature: a textbook in basic ecology</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">R</forename>
                                    <forename type="middle">E</forename>
                                    <surname>Ricklefs</surname>
                                </persName>
                            </author>
                            <imprint>
                                <date type="published" when="1990" />
                                <publisher>Freeman and Co</publisher>
                                <biblScope unit="page" from="516" to="517" />
                                <pubPlace>New York</pubPlace>
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b33">
                        <monogr>
                            <title level="m" type="main">The mathematical theory of communication</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">C</forename>
                                    <forename type="middle">E</forename>
                                    <surname>Shannon</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">W</forename>
                                    <surname>Weaver</surname>
                                </persName>
                            </author>
                            <imprint>
                                <date type="published" when="1949" />
                                <publisher>Univ. of Ill. Press</publisher>
                                <pubPlace>Urbana, IL</pubPlace>
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b34">
                        <analytic>
                            <title level="a" type="main">Reservoir effects on downstream river channel migration</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">F</forename>
                                    <forename type="middle">D</forename>
                                    <surname>Shields</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">A</forename>
                                    <surname>Simon</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">L</forename>
                                    <forename type="middle">J</forename>
                                    <surname>Steffen</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Environmental Conservation</title>
                            <imprint>
                                <biblScope unit="volume">27</biblScope>
                                <biblScope unit="issue">1</biblScope>
                                <biblScope unit="page" from="54" to="66" />
                                <date type="published" when="2000" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b35">
                        <analytic>
                            <title level="a" type="main">Short-term changes in channel form and macroinvertebrate communities following low-head dam removal</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">E</forename>
                                    <forename type="middle">H</forename>
                                    <surname>Stanley</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">M</forename>
                                    <forename type="middle">A</forename>
                                    <surname>Luebke</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">M</forename>
                                    <forename type="middle">W</forename>
                                    <surname>Doyle</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">D</forename>
                                    <forename type="middle">W</forename>
                                    <surname>Marshall</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Journal of the North American Benthological Society</title>
                            <imprint>
                                <biblScope unit="volume">21</biblScope>
                                <biblScope unit="issue">1</biblScope>
                                <biblScope unit="page" from="172" to="187" />
                                <date type="published" when="2002" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b36">
                        <analytic>
                            <title level="a" type="main">Riverine ecosystems: the influence of man on catchment dynamics and fish ecology</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">V</forename>
                                    <surname>Ward</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">J</forename>
                                    <forename type="middle">A</forename>
                                    <surname>Stanford</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="m">Proceedings of the International Large River Symposium</title>
                            <meeting>the International Large River Symposium</meeting>
                            <imprint>
                                <date type="published" when="1989" />
                                <biblScope unit="volume">106</biblScope>
                            </imprint>
                        </monogr>
                        <note>Pages 56-64 in D.P. Dodge editor</note>
                    </biblStruct>
                    <biblStruct xml:id="b37">
                        <analytic>
                            <title level="a" type="main">A scale of grade and class for elastic sediments</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">C</forename>
                                    <forename type="middle">K</forename>
                                    <surname>Wentworth</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Journal of Geology</title>
                            <imprint>
                                <biblScope unit="volume">30</biblScope>
                                <biblScope unit="page" from="377" to="392" />
                                <date type="published" when="1922" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b38">
                        <monogr>
                            <title level="m" type="main">Downstream effects of dams on alluvial rivers</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">G</forename>
                                    <forename type="middle">P</forename>
                                    <surname>Williams</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">M</forename>
                                    <forename type="middle">G</forename>
                                    <surname>Wolman</surname>
                                </persName>
                            </author>
                            <imprint>
                                <date type="published" when="1984" />
                                <pubPlace>Washington, D.C.: U.S. Geological Survey</pubPlace>
                            </imprint>
                        </monogr>
                        <note>Professional paper 1286</note>
                    </biblStruct>
                    <biblStruct xml:id="b39">
                        <analytic>
                            <title level="a" type="main">A method of sampling coarse river-bed material</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">M</forename>
                                    <forename type="middle">G</forename>
                                    <surname>Wolman</surname>
                                </persName>
                            </author>
                        </analytic>
                        <monogr>
                            <title level="j">Transactions of the American Geophysical Union</title>
                            <imprint>
                                <biblScope unit="volume">35</biblScope>
                                <biblScope unit="issue">6</biblScope>
                                <biblScope unit="page" from="951" to="956" />
                                <date type="published" when="1954" />
                            </imprint>
                        </monogr>
                    </biblStruct>
                    <biblStruct xml:id="b40">
                        <monogr>
                            <title level="m" type="main">Consulting firm responsible of the removal of the Randall Dam on the Coldwater River</title>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">D</forename>
                                    <forename type="middle">A</forename>
                                    <surname>Zebell</surname>
                                </persName>
                            </author>
                            <author>
                                <persName
                                    xmlns="http://www.tei-c.org/ns/1.0">
                                    <forename type="first">P</forename>
                                    <forename type="middle">C</forename>
                                    <surname>Lawson-Fisher Associates</surname>
                                </persName>
                            </author>
                            <imprint>
                                <date type="published" when="2002" />
                                <pubPlace>Branch Co., MI</pubPlace>
                            </imprint>
                        </monogr>
                        <note>Personal Communication. Senior Civil Engineer</note>
                    </biblStruct>
                </listBibl>
            </div>
        </back>
    </text>
</TEI>
```

