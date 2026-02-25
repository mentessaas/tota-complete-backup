#!/usr/bin/env python3
"""
Feedback Analyzer - Analiza resultados y propone mejoras
Usage: python3 feedback_analyze.py [type]
Types: trade, email, lead, job (default: all)
"""
import sys
import json
import os
from datetime import datetime, timedelta
from collections import Counter

BASE_DIR = os.path.expanduser("~/zaltyko-os/feedback")

def load_entries(type_name=None, days=7):
    all_entries = []
    folder_map = {
        "trade": "trades",
        "email": "emails",
        "lead": "leads",
        "job": "jobs",
        "all": ["trades", "emails", "leads", "jobs"]
    }
    
    folders = folder_map.get(type_name, ["trades", "emails", "leads", "jobs"]) if type_name == "all" else [folder_map.get(type_name, type_name)]
    
    for folder in folders:
        folder_path = f"{BASE_DIR}/{folder}"
        if not os.path.exists(folder_path):
            continue
            
        for i in range(days):
            date = (datetime.now() - timedelta(days=i)).strftime('%Y%m%d')
            file_path = f"{folder_path}/{date}.jsonl"
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    for line in f:
                        try:
                            all_entries.append(json.loads(line))
                        except:
                            pass
    return all_entries

def analyze_trades(entries):
    trades = [e for e in entries if e.get('type') == 'trade']
    if not trades:
        return "No trade data"
    
    results = Counter([e.get('result') for e in trades])
    total = len(trades)
    success_rate = results.get('success', 0) / total * 100 if total > 0 else 0
    
    insights = []
    insights.append(f"📊 Trades: {total} | Win rate: {success_rate:.1f}%")
    
    # Analizar losses
    losses = [e for e in trades if e.get('result') == 'failure']
    if losses:
        reasons = []
        for e in losses:
            details = e.get('details', '')
            if isinstance(details, dict):
                reasons.append(details.get('reason', 'unknown'))
            elif isinstance(details, str):
                if 'reason:' in details:
                    reasons.append(details.split('reason:')[1].split(',')[0])
                else:
                    reasons.append('unknown')
            else:
                reasons.append('unknown')
        top_reasons = Counter(reasons).most_common(3)
        if top_reasons:
            insights.append(f"❌ Losses: {len(losses)}. Top reasons: {', '.join([f'{r}({c})' for r,c in top_reasons])}")
    
    return "\n".join(insights)

def analyze_emails(entries):
    emails = [e for e in entries if e.get('type') == 'email']
    if not emails:
        return "No email data"
    
    results = Counter([e.get('result') for e in emails])
    total = len(emails)
    open_rate = results.get('opened', 0) / total * 100 if total > 0 else 0
    reply_rate = results.get('reply', 0) / total * 100 if total > 0 else 0
    
    insights = []
    insights.append(f"📧 Emails: {total} | Open: {open_rate:.1f}% | Reply: {reply_rate:.1f}%")
    
    # Analizar que funciona mejor
    successful = [e for e in emails if e.get('result') in ['reply', 'opened']]
    if successful:
        # Handle both string and dict details
        templates = []
        for e in successful:
            details = e.get('details', '')
            if isinstance(details, dict):
                templates.append(details.get('template', 'unknown'))
            elif isinstance(details, str):
                # Extract template from string if present
                if 'template:' in details:
                    templates.append(details.split('template:')[1].split(',')[0])
                else:
                    templates.append('unknown')
            else:
                templates.append('unknown')
        top_templates = Counter(templates).most_common(3)
        if top_templates:
            insights.append(f"✅ Best templates: {', '.join([f'{t}({c})' for t,c in top_templates])}")
    
    return "\n".join(insights)

def analyze_leads(entries):
    leads = [e for e in entries if e.get('type') == 'lead']
    if not leads:
        return "No lead data"
    
    results = Counter([e.get('result') for e in leads])
    total = len(leads)
    valid_rate = results.get('valid', 0) / total * 100 if total > 0 else 0
    
    insights = []
    insights.append(f"🎯 Leads: {total} | Valid: {valid_rate:.1f}%")
    
    # Sources - handle both string and dict
    sources = []
    for e in leads:
        details = e.get('details', '')
        if isinstance(details, dict):
            sources.append(details.get('source', 'unknown'))
        elif isinstance(details, str):
            if 'source:' in details:
                sources.append(details.split('source:')[1].split(',')[0])
            else:
                sources.append('unknown')
        else:
            sources.append('unknown')
    
    top_sources = Counter(sources).most_common(3)
    if top_sources:
        insights.append(f"📍 Top sources: {', '.join([f'{s}({c})' for s,c in top_sources])}")
    
    return "\n".join(insights)

def analyze_jobs(entries):
    jobs = [e for e in entries if e.get('type') == 'job']
    if not jobs:
        return "No job data"
    
    results = Counter([e.get('result') for e in jobs])
    total = len(jobs)
    success_rate = results.get('success', 0) / total * 100 if total > 0 else 0
    
    insights = []
    insights.append(f"⚙️ Jobs: {total} | Success: {success_rate:.1f}%")
    
    failures = [e for e in jobs if e.get('result') == 'failure']
    if failures:
        errors = []
        for e in failures:
            details = e.get('details', '')
            if isinstance(details, dict):
                errors.append(details.get('error', 'unknown'))
            elif isinstance(details, str):
                if 'error:' in details:
                    errors.append(details.split('error:')[1].split(',')[0])
                else:
                    errors.append('unknown')
            else:
                errors.append('unknown')
        top_errors = Counter(errors).most_common(3)
        if top_errors:
            insights.append(f"❌ Common errors: {', '.join([f'{e}({c})' for e,c in top_errors])}")
    
    return "\n".join(insights)

def generate_recommendations(entries):
    """Genera recomendaciones basadas en los datos"""
    recs = []
    
    # Trades
    trades = [e for e in entries if e.get('type') == 'trade']
    if trades:
        losses = [e for e in trades if e.get('result') == 'failure']
        if len(losses) > len(trades) * 0.5:
            recs.append("🔴 Trades: >50% losses. Revisar estrategia de señales.")
    
    # Emails
    emails = [e for e in entries if e.get('type') == 'email']
    if emails:
        replies = [e for e in emails if e.get('result') == 'reply']
        if len(replies) < len(emails) * 0.05:
            recs.append("🔴 Emails: <5% reply rate. Probar nuevos templates.")
    
    # Leads
    leads = [e for e in entries if e.get('type') == 'lead']
    if leads:
        valid = [e for e in leads if e.get('result') == 'valid']
        if len(valid) > len(leads) * 0.7:
            recs.append("✅ Leads: >70% válidos. Fuente funcionando bien.")
    
    return recs

def main():
    type_name = sys.argv[1] if len(sys.argv) > 1 else "all"
    days = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    
    entries = load_entries(type_name, days)
    
    if not entries:
        print(f"📭 No feedback data for last {days} days")
        return
    
    print(f"📊 Feedback Analysis - Last {days} days\n")
    print(f"Total entries: {len(entries)}\n")
    
    if type_name in ["all", "trade"]:
        print(analyze_trades(entries))
        print()
    
    if type_name in ["all", "email"]:
        print(analyze_emails(entries))
        print()
    
    if type_name in ["all", "lead"]:
        print(analyze_leads(entries))
        print()
    
    if type_name in ["all", "job"]:
        print(analyze_jobs(entries))
        print()
    
    # Recommendations
    recs = generate_recommendations(entries)
    if recs:
        print("💡 RECOMMENDATIONS:")
        for r in recs:
            print(r)

if __name__ == "__main__":
    main()
