import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Cloud Text Checker",
    page_icon="☁️",
    layout="centered",
)

st.title("☁️ Cloud Text Checker")
st.caption("A simple one-file Streamlit app for the Cloud Computing mini project.")

st.info(
    "Type a message below. This demo uses a small rule-based check to flag common "
    "spam-like phrases; it is for learning only and is not a trained machine-learning model."
)

message = st.text_area(
    "Enter a message to check",
    placeholder="Example: Congratulations! You have won a free prize. Click now!",
    height=150,
)

spam_phrases = [
    "claim your prize",
    "you have won",
    "won a prize",
    "free money",
    "click now",
    "limited time",
    "act now",
    "urgent",
    "verify your account",
    "send otp",
    "cash prize",
    "congratulations",
]

if st.button("Check message", type="primary", use_container_width=True):
    if not message.strip():
        st.warning("Please enter a message first.")
    else:
        normalized = message.lower()
        matched = [phrase for phrase in spam_phrases if phrase in normalized]
        # Also flag messages containing several exclamation marks or many links.
        extra_signals = 0
        if message.count("!") >= 3:
            extra_signals += 1
        if normalized.count("http://") + normalized.count("https://") >= 2:
            extra_signals += 1

        score = len(matched) + extra_signals
        if score >= 2:
            st.error("Result: This message looks suspicious / spam-like.")
        elif score == 1:
            st.warning("Result: This message may be spam. Review it carefully.")
        else:
            st.success("Result: No common spam signals were found.")

        if matched:
            st.write("**Matched phrases:** " + ", ".join(f"`{p}`" for p in matched))
        else:
            st.write("**Matched phrases:** None")
        st.caption("This result is a simple rule-based estimate, not a guarantee.")

st.divider()
st.subheader("Cloud service models — in 3 lines")
st.markdown(
    "- **IaaS (Infrastructure as a Service):** rents virtual machines, storage, and networks; "
    "you manage the operating system and applications.\n"
    "- **PaaS (Platform as a Service):** provides a managed platform to deploy code without "
    "managing most servers or operating systems.\n"
    "- **SaaS (Software as a Service):** provides a ready-to-use application over the internet."
)
st.write(
    "**Why Streamlit Community Cloud is PaaS:** it provides a managed environment to deploy "
    "a Streamlit app from GitHub, while the platform handles much of the hosting infrastructure."
)

st.divider()
st.subheader("Examples of cloud-provider free offers")
st.caption(
    "Offers change by region, account type, and date. Check each provider's official page "
    "before relying on credits or limits."
)
free_tier_rows = [
    {
        "Provider": "AWS",
        "Free offer (examples)": "Free plan / selected services and introductory credits or trials, depending on eligibility",
        "Official page": "https://aws.amazon.com/free/",
    },
    {
        "Provider": "Microsoft Azure",
        "Free offer (examples)": "Eligible new customers may receive starting credit plus selected services free for limited periods",
        "Official page": "https://azure.microsoft.com/pricing/free-services/",
    },
    {
        "Provider": "Google Cloud",
        "Free offer (examples)": "Eligible new customers may receive trial credit; selected products also have free usage limits",
        "Official page": "https://cloud.google.com/free",
    },
]
st.table(free_tier_rows)

st.caption(f"Mini project demo • Last opened: {datetime.now().strftime('%d %b %Y')}")
