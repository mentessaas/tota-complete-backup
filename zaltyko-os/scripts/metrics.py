#!/usr/bin/env python3
"""
Metrics Tracker - Seguimiento de KPIs
Usage: python3 metrics.py [days]
"""
import sys
import json
import os
from datetime import datetime, timedelta
from collections import defaultdict

BASE_DIR = os.path.expanduser("~/zaltyko-os/feedback")

def calculate_metrics(days=7):
    metrics = {
        "period": f"Last {days} days",
        "generated_at": datetime.now().isoformat(),
        "trades": {},
        "emails": {},
        "leads": {},
        "jobs": {}
    }
    
    # Load all entries
    all_entries = []
    for folder in ["trades", "emails", "leads", "jobs"]:
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
    
    # Calculate metrics
    for type_name in ["trades", "emails", "leads", "jobs"]:
        entries = [e for e in all_entries if e.get('type') == type_name]
        if not entries:
            continue
        
        total = len(entries)
        results = defaultdict(int)
        for e in entries:
            results[e.get('result', 'unknown')] += 1
        
        metrics[type_name] = {
            "total": total,
            "success_rate": results.get('success', 0) / total * 100 if total > 0 else 0,
            "results": dict(results)
        }
    
    return metrics

def main():
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    
    metrics = calculate_metrics(days)
    
    print("📊 METRICS DASHBOARD")
    print(f"Period: {metrics['period']}")
    print(f"Generated: {metrics['generated_at']}\n")
    
    # Trades
    if metrics.get('trades', {}).get('total', 0) > 0:
        t = metrics['trades']
        print(f"📈 TRADES: {t['total']} | Win Rate: {t['success_rate']:.1f}%")
    
    # Emails
    if metrics.get('emails', {}).get('total', 0) > 0:
        e = metrics['emails']
        print(f"📧 EMAILS: {e['total']} | Success: {e['success_rate']:.1f}%")
    
    # Leads
    if metrics.get('leads', {}).get('total', 0) > 0:
        l = metrics['leads']
        print(f"🎯 LEADS: {l['total']} | Valid: {l['success_rate']:.1f}%")
    
    # Jobs
    if metrics.get('jobs', {}).get('total', 0) > 0:
        j = metrics['jobs']
        print(f"⚙️ JOBS: {j['total']} | Success: {j['success_rate']:.1f}%")
    
    # Save to file
    os.makedirs(BASE_DIR, exist_ok=True)
    with open(f"{BASE_DIR}/metrics_latest.json", 'w') as f:
        json.dump(metrics, f, indent=2)
    
    print(f"\n✅ Saved to {BASE_DIR}/metrics_latest.json")

if __name__ == "__main__":
    main()
