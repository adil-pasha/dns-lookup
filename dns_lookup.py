import streamlit as st
import dns.resolver

st.title("Simple DNS Lookup Tool")
domain = st.text_input("Enter domain (e.g. example.com):")

records_to_query = ["A", "AAAA", "MX", "NS", "CNAME", "TXT"]

if domain:
    st.header("DNS Records")
    for rtype in records_to_query:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            st.write(f"{rtype} records:")
            for r in answers:
                st.write(str(r))
        except Exception as e:
            st.write(f"{rtype}: Not found or error")