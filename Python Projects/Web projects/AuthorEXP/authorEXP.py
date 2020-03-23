from Bio import Entrez
import scholarly
import re
from google_images_download import google_images_download


def request_idList(string):
    """
    Gets an ID List of papers which the author has contributed to
    :param string:
    :return:
    """
    Entrez.email = "maximustinovburner@gmail.com"
    handle = Entrez.esearch(db="pubmed", term=string, retmax=200)
    record = Entrez.read(handle)
    handle.close()
    if len(record["IdList"]) == 0:
        print("No results found")
    return record["IdList"]


solo_author = [[] for _ in range(3)]
last_author = [[] for _ in range(3)]
first_author = [[] for _ in range(3)]
name = str
IDList = []

def request_pubmed(string):
    """
    Gets Keywords and MeSH Headings from the articles in IDList
    :param string:
    :return:
    """
    cleaned_keywords = []
    cleaned_meshHeadings = []
    global solo_author
    global last_author
    global first_author
    global name
    global IDList
    IDList = request_idList(string)
    if not IDList:
        errorhelp = ""
        return errorhelp

    Entrez.email = "ge39nuy@mytum.de"
    handle = Entrez.efetch(db="pubmed", id=IDList, rettype="null", retmode="xml")
    record = Entrez.read(handle)
    handle.close()
    article_list = record['PubmedArticle']
    for x in range(len(IDList)):
        single_article = article_list[x]
        medline_citation = single_article['MedlineCitation']
        keyword_list_nested = medline_citation.get('KeywordList')
        article_data = medline_citation['Article']
        author_list = article_data.get('AuthorList')
        try:
            article_title_text = article_data.get('ArticleTitle')
            article_title_re = re.sub(r'(<\w*>)', "", article_title_text)
            article_title_re2 = re.sub(r'(</\w*>)', "", article_title_re)
            article_title = "".join(article_title_re2)
        except:
            pass
        try:
            article_abstract_doublenested = article_data.get('Abstract')
            article_abstract_nested = article_abstract_doublenested.get('AbstractText')
            article_abstract_text = article_abstract_nested[0]
            article_abstract_text_re = re.sub(r'(<\w*>)', "", article_abstract_text)
            article_abstract_text_re2 = re.sub(r'(</\w*>)', "", article_abstract_text_re)
            article_abstract = "".join(article_abstract_text_re2)
        except:
            pass

        def lists():
            try:
                keyword_list = keyword_list_nested[0]
                for n in range(len(keyword_list)):
                    key = "".join(keyword_list[n])
                    cleaned_keywords.append(key)
            except:
                pass
            try:
                mesh_heading_list = single_article['MedlineCitation'].get('MeshHeadingList')
                for i in range(len(mesh_heading_list)):
                    mesh = "".join(mesh_heading_list[i].get('DescriptorName'))
                    cleaned_meshHeadings.append(mesh)
            except:
                pass

        for y in range(len(author_list)):
            forename = "".join(str(author_list[y].get('ForeName')))
            fullname = forename + " " + str(author_list[y].get('LastName'))
            if string.lower() == fullname.lower():
                name = fullname
                if y == 0 == len(author_list) - 1:
                    for _ in range(5):
                        lists()
                    solo_author[0].append(IDList[x])
                    solo_author[2].append(article_abstract)
                    solo_author[1].append(article_title)
                    break
                if y == 0:
                    for _ in range(2):
                        lists()
                    first_author[0].append(IDList[x])
                    first_author[2].append(article_abstract)
                    first_author[1].append(article_title)
                if y == len(author_list) - 1:
                    for _ in range(3):
                        lists()
                    last_author[0].append(IDList[x])
                    last_author[2].append(article_abstract)
                    last_author[1].append(article_title)
            else:
                continue
        lists()
    combined_list = cleaned_meshHeadings + cleaned_keywords
    sorted_list = sorted(combined_list, key=combined_list.count, reverse=True)
    weighted_list = [word for word in sorted_list if sorted_list.count(word) > len(IDList) // 10]
    final_list = list(dict.fromkeys(weighted_list))

    filter_words = ['Female', 'Humans', 'Animals', 'Adult', 'Adolescent', 'Internet', 'Male', 'Models']
    filtered_list = [word for word in final_list if word not in filter_words]  # damn this looks good
    return filtered_list


def request_scholar(string):
    try:
        search_query = scholarly.search_author(string)
        author = next(search_query)
        author1 = author.interests
        try:
            author = next(search_query)
            author = ["The results could be wrong, because there are mutliple authors with similar names in the google scholar database", author.interests, author1]
            return author
        except:
            pass
        author = author1

        return author
    except:
        pass


def clear():
    global solo_author
    solo_author = [[] for _ in range(3)]
    global last_author
    last_author = [[] for _ in range(3)]
    global first_author
    first_author = [[] for _ in range(3)]
    global IDList
    IDList = []


def mugshot(string):
    try:
        response = google_images_download.googleimagesdownload()
        image_paths = response.download({"keywords": string, "limit": 1, "no_download": True})
        paths = []
        for k, v in image_paths[0].items():
            paths += v
        img = "".join(paths[0])
        return img
    except:
        pass
