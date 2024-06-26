tit_xpath = '//*[@id="search_result"]/ul/li[*]/div[1]/div[1]/a'
contents_no = 0
page_no = 0

while True : 
    page_no += 1
    print(f'========= {page_no} 페이지 스크래핑 시작 =========')
    mylist = driver.find_elements(By.XPATH, tit_xpath)

    for i in range(len(mylist)):
        contents_no += 1
        print(contents_no, mylist[i].text)
    
    if no % 50 == 0:
        driver.find_element(By.CSS_SELECTOR, '.btn_next').click()
        time.sleep(3)
        continue

    try : # 다음 페이지 버튼이 없을 경우 예외처리
        next_button = driver.find_element(By.CSS_SELECTOR, f"a[id='{page_no+1}']")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(3)
    except Exception as e:
        print('='*50)
        print(f'{page_no+1}페이지 버튼 클릭시 예외가 발생했습니다.', e)
        print('===== 데이터를 저장하고 프로그램을 종료합니다. =====')
        break     
        
print(f'========= 총 {page_no}페이지 {contents_no}개 데이터 스크래핑 완료 =========')