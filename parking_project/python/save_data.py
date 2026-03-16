import pandas as pd
import sqlite3

csv_file = "전국주차장정보표준데이터.csv"
db_file = "parking_master.db"  # 원하는 DB 이름

try:
    # 1. CSV 파일 읽기
    print("⏳ CSV 파일을 읽는 중입니다. 데이터가 많아 몇 초 정도 걸릴 수 있습니다...")
    df = pd.read_csv(csv_file, encoding="cp949")

    # 2. DB 연결
    conn = sqlite3.connect(db_file)

    # 3. 테이블 저장
    df.to_sql("national_parking", conn, if_exists="replace", index=False)

    print(f"🎉 성공! 총 {len(df):,}개의 전국 주차장 데이터가 '{db_file}'의 'national_parking' 테이블에 저장되었습니다.")

except UnicodeDecodeError:
    # cp949로 안 읽히면 utf-8로 재시도
    print("🔄 인코딩 방식이 달라 utf-8로 다시 시도합니다...")
    
    df = pd.read_csv(csv_file, encoding="utf-8")
    conn = sqlite3.connect(db_file)

    df.to_sql("national_parking", conn, if_exists="replace", index=False)

    print(f"🎉 성공! 총 {len(df):,}개의 전국 주차장 데이터가 '{db_file}'에 저장되었습니다.")

except Exception as e:
    print(f"❌ 에러가 발생했습니다: {e}")

finally:
    # DB 연결 종료
    if "conn" in locals():
        conn.close()