import subprocess
import time

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import requests
from scrapy.crawler import CrawlerProcess

from .models import Links, JobDetail


# Create your views here.

def request_url(request):
    url = "https://remote.co/remote-jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', class_='btn-category')[1:]
    visited_links = set()

    for link in links:
        href_link = link.get('href')
        if href_link is not None:
            if "/remote-jobs/" in href_link:
                jobs_category = "https://remote.co" + href_link
                if jobs_category not in visited_links:
                    visited_links.add(jobs_category)
        else:
            print("Not Avaialble")
    # import pdb;
    # pdb.set_trace()
    list_visit = list(visited_links)
    category_length = len(list_visit)
    category = list_visit[1]
    response_category = requests.get(category)
    soup_category = BeautifulSoup(response_category.content, 'html.parser')
    category_links = soup_category.find_all('a', class_='border-bottom')
    category_visited_links = set()

    for category_link in category_links:
        category_href_link = category_link.get('href')
        if category_href_link is not None:
            if "/job/" in category_href_link:
                category_jobs = "https://remote.co" + category_href_link
                if category_jobs not in category_visited_links:
                    category_visited_links.add(category_jobs)
        else:
            print("Not Avaialble")
    category_visited_links_list = list(category_visited_links)
    # print("JOB ACCORDING TO CATEGORY: ", category_visited_links_list)
    category_visited_links_length = len(category_visited_links_list)
    jobs = category_visited_links_list[1] or category_visited_links_list[0]
    # print(jobs, "JOBS links")
    # print()
    response_job = requests.get(jobs)
    soup_job = BeautifulSoup(response_job.content, 'html.parser')

    job_title_element = soup_job.select_one('div.card-body h1.font-weight-bold')
    job_title = job_title_element.get_text() if job_title_element else "Not Available"

    # Extracting location
    location_element = soup_job.select_one('div.location_sm strong')
    location = location_element.get_text().strip() if location_element else "Not Available"

    # Extracting Salary
    salary_element = soup_job.select_one('div.col-10 col-sm-11 pl-1')
    salary = salary_element.get_text().strip() if salary_element else "Not Available"

    # Extracting posted date
    posted_date_element = soup_job.select_one('div.date_tags time')
    posted_date = posted_date_element['datetime'] if posted_date_element else "Not Available"

    # Extracting job types
    job_types_elements = soup_job.select('div.date_tags span.job_flag')
    job_types = [job_type.get_text() for job_type in job_types_elements]

    # Extracting job description
    job_description_element = soup_job.select_one('div.job_description')
    job_description = job_description_element.get_text() if job_description_element else "Not Available"

    # Extracting company name and company website link
    company_name_element = soup_job.select_one('div.company_sm div.co_name strong')
    company_name = company_name_element.get_text() if company_name_element else "Not Available"

    company_website_element = soup_job.select_one('div.company_sm div.links_sm a[href]')
    company_website = company_website_element['href'] if company_website_element else "Not Available"

    # Extracting job price per hour
    price_per_hour_element = soup_job.select_one('div.job_description strong:contains("$")')
    price_per_hour = price_per_hour_element.get_text() if price_per_hour_element else "Not Available"

    salary_element_test = soup.select_one('p:contains("Rate/Salary:")')
    salary_test = salary_element_test.get_text().replace("Rate/Salary:",
                                                         "").strip() if salary_element_test else "Not Available"

    # Print the extracted information
    data = {
        "Job Title": job_title,
        "Location": location,
        "Posted Date": posted_date,
        "Job Types": job_types,
        "Job Description": job_description,
        "Company Name": company_name,
        "Company Website": company_website,
        "Price per Hour": price_per_hour,
        "Salary": salary,
        "salary_element_test": salary_test,
    }
    print(data)
    return JsonResponse(data)


# Your imports and other parts of the code remain the same

def final_url(request):
    url = "https://remote.co/remote-jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', class_='btn-category')[1:]
    visited_links = set()

    for link in links:
        href_link = link.get('href')
        if href_link is not None and "/remote-jobs/" in href_link:
            jobs_category = "https://remote.co" + href_link
            visited_links.add(jobs_category)

    list_visit = list(visited_links)
    category_length = len(list_visit)
    current_category_index = 0

    while current_category_index < category_length:
        category = list_visit[current_category_index]
        response_category = requests.get(category)
        soup_category = BeautifulSoup(response_category.content, 'html.parser')
        category_links = soup_category.find_all('a', class_='border-bottom')
        category_visited_links = set()

        for category_link in category_links:
            category_href_link = category_link.get('href')
            if category_href_link is not None and "/job/" in category_href_link:
                category_jobs = "https://remote.co" + category_href_link
                category_visited_links.add(category_jobs)

        category_visited_links_list = list(category_visited_links)
        category_visited_links_length = len(category_visited_links_list)
        current_job_index = 0

        while current_job_index < category_visited_links_length:
            jobs = category_visited_links_list[current_job_index]
            response_job = requests.get(jobs)
            soup_job = BeautifulSoup(response_job.content, 'html.parser')

            job_title_element = soup_job.select_one('div.card-body h1.font-weight-bold')
            job_title = job_title_element.get_text() if job_title_element else "Not Available"

            # Extracting location
            # location_element = soup_job.select_one('div.location_sm strong')
            location_element = soup_job.select_one('div.location_sm')
            location = location_element.get_text().strip() if location_element else "Not Available"

            # Extracting Salary
            salary_element = soup_job.select_one('div.col-10 col-sm-11 pl-1')
            salary = salary_element.get_text().strip() if salary_element else "Not Available"

            # Extracting posted date
            posted_date_element = soup_job.select_one('div.date_tags time')
            posted_date = posted_date_element['datetime'] if posted_date_element else "Not Available"

            #get job types 
            job_value = set()
            job_type = soup_job.find_all('a', class_='job_flag')
            for job in job_type:
                job_value.add(job.get_text())
            job_types_str = str(job_value)
            job_types = job_types_str.replace("{", '').replace("}", '')
           
           #job Description 
            job_description_element = soup_job.select_one('div.job_description')
            job_description = job_description_element.get_text() if job_description_element else "Not Available"

            # Extracting company name and company website link
            company_name_element = soup_job.select_one('div.company_sm div.co_name strong')
            company_name = company_name_element.get_text() if company_name_element else "Not Available"

            company_website_element = soup_job.select_one('div.company_sm div.links_sm a[href]')
            company_website = company_website_element['href'] if company_website_element else "Not Available"



            logo_tag = soup_job.find_all('img', class_='job_company_logo')
            for logos in logo_tag:
                logo_url = logos['src']
                # print(logo_url)
                # print("========================================================")
            # print("Logo_tag", logo_tag)

            # if logo_tag:
            #     logo_url = logo_tag['src']
            # else:
            #     logo_url = "Not Available"
            # logo_url = company_logo['src'] if company_logo else "Not Available"
            # logo_url = soup_job.get('a', class_='job_company_logo')
            # company_name = soup_job.css('img.job_company_logo::attr(alt)').get()
            # logo_url = "https://remoteco.s3.amazonaws.com/wp-content/uploads/2023/06/09213220/Red-River-Logo-150x150.jpeg"
            # Extracting job price per hour
            price_per_hour_element = soup_job.select_one('div.job_description strong:contains("$")')
            price_per_hour = price_per_hour_element.get_text() if price_per_hour_element else "Not Available"

            salary_element_test = soup_job.select_one('p:contains("Rate/Salary:")')
            salary_test = salary_element_test.get_text().replace("Rate/Salary:",
                                                                 "").strip() if salary_element_test else "Not Available"
            apply_link_element = soup_job.find('a', id='apply_button_gtm')
            apply_link = apply_link_element.get('href') if apply_link_element else "Not Available"

            category_link = category.replace("https://remote.co/remote-jobs/", '')
            fcategory = category_link.replace('/', '')

            company_location = location.replace('Location', '').replace(':', '').replace('Remote', '').replace(',', '')

            if not JobDetail.objects.filter(job_link=jobs).exists():
                values = JobDetail.objects.create(job_title=job_title, job_address=location, job_created_at=posted_date,
                                                  type=job_types, job_description_format=job_description,
                                                  company_name=company_name, company_website=company_website,
                                                  price_per_hour=price_per_hour, salary=salary,company_logo=logo_url,
                                                  category=fcategory, job_link=jobs, wpjobboard_am_data=apply_link, company_location=company_location)
                values.save()
            else:
                print("Data Already Exists !!")

            current_job_index += 1

        current_category_index += 1
    return HttpResponse("Web scraping completed!")






import scrapy
from .models import JobDetail
from urllib.parse import urljoin


# from scrapy_djangoitem import DjangoCrawlerProcess

class RemoteJobsSpider(scrapy.Spider):
    name = "remote_jobs"

    def start_requests(self):
        url = "https://remote.co/remote-jobs/"
        yield scrapy.Request(url, self.parse_category)

    def parse_category(self, response):
        category_links = response.css('a.btn-category::attr(href)').extract()

        for link in category_links:
            yield scrapy.Request(urljoin(response.url, link), self.parse_job_links)

    def parse_job_links(self, response):
        job_links = response.css('a.border-bottom::attr(href)').extract()

        for job_link in job_links:
            yield scrapy.Request(urljoin(response.url, job_link), self.parse_job)

    def parse_job(self, response):
        job_title = response.css('div.card-body h1.font-weight-bold::text').get(default="Not Available")

        location_element = response.css('div.location_sm::text').get()
        location = location_element.strip() if location_element else "Not Available"

        salary = response.css('div.col-10.col-sm-11.pl-1::text').get(default="Not Available")

        posted_date = response.css('div.date_tags time::attr(datetime)').get(default="Not Available")

        job_types = response.css('div.date_tags span.job_flag::text').extract()

        job_description = response.css('div.job_description::text').get(default="Not Available")

        company_name = response.css('div.company_sm div.co_name strong::text').get(default="Not Available")

        company_website = response.css('div.company_sm div.links_sm a[href]::attr(href)').get(default="Not Available")

        price_per_hour = response.css('div.job_description strong:contains("$")::text').get(default="Not Available")

        salary_element_test = response.css('p:contains("Rate/Salary:")::text').get()
        salary_test = salary_element_test.replace("Rate/Salary:",
                                                  "").strip() if salary_element_test else "Not Available"

        apply_link_element = response.css('a#apply_button_gtm::attr(href)').get(default="Not Available")
        apply_link = urljoin(response.url, apply_link_element)

        category_link = response.url.replace("https://remote.co/remote-jobs/", '')
        print(category_link, "==============")
        import pdb;
        pdb.set_trace()
        if not JobDetail.objects.filter(job_link=response.url).exists():
            values = JobDetail.objects.create(
                job_title=job_title,
                location=location,
                posted_date=posted_date,
                job_types=job_types,
                job_description=job_description,
                company_name=company_name,
                company_website=company_website,
                price_per_hour=price_per_hour,
                salary=salary,
                category=category_link,
                job_link=response.url,
                apply_link=apply_link
            )
            values.save()
        else:
            self.log("Values error !")

        yield {
            'job_title': job_title,
            'location': location,
            'posted_date': posted_date,
            'job_types': job_types,
            'job_description': job_description,
            'company_name': company_name,
            'company_website': company_website,
            'price_per_hour': price_per_hour,
            'salary': salary,
            'category': category_link,
            'job_link': response.url,
            'apply_link': apply_link,
        }


def scrape_remote_jobs(request):
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    })

    # Run the Scrapy spider
    process.crawl(RemoteJobsSpider)
    process.start()

    return HttpResponse("Web scraping completed!")
# def scrape_remote_jobs(request):
