#!/usr/bin/env python3
"""
Transcriber - Extrae transcripciones de videos (PROPIO, gratis)
"""
import sys
import re
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url):
    patterns = [
        r'(?:youtube\.com/watch\?v=)([a-zA-Z0-9_-]{11})',
        r'(?:youtu\.be/)([a-zA-Z0-9_-]{11})',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def get_transcript(url, language='es'):
    video_id = extract_video_id(url)
    if not video_id:
        return {"error": "URL de YouTube inválida"}
    
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=[language, 'en'])
        
        # Extraer texto de cada snippet
        full_text = ""
        for snippet in transcript.snippets:
            full_text += snippet.text + " "
        
        return {
            "video_id": video_id,
            "transcript": full_text.strip(),
            "segments": len(transcript.snippets),
            "language": transcript.language
        }
    except Exception as e:
        return {"error": str(e)}

def get_formatted(url, language='es'):
    video_id = extract_video_id(url)
    if not video_id:
        return {"error": "URL inválida"}
    
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=[language, 'en'])
        
        formatted = []
        for snippet in transcript.snippets:
            minutes = int(snippet.start // 60)
            seconds = int(snippet.start % 60)
            timestamp = f"{minutes:02d}:{seconds:02d}"
            formatted.append(f"[{timestamp}] {snippet.text}")
        
        return {
            "video_id": video_id,
            "formatted": "\n".join(formatted),
            "segments": len(transcript.snippets)
        }
    except Exception as e:
        return {"error": str(e)}

# CLI
def main():
    if len(sys.argv) < 3:
        print("Uso: python3 transcriber.py get <url>")
        print("      python3 transcriber.py format <url>")
        return
    
    cmd = sys.argv[1]
    url = sys.argv[2]
    
    if cmd == "get":
        result = get_transcript(url)
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print(f"📝 {result['segments']} segmentos, idioma: {result['language']}")
            print("-" * 50)
            print(result['transcript'][:1500])
    
    elif cmd == "format":
        result = get_formatted(url)
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print(f"📝 {result['segments']} segmentos")
            print("-" * 50)
            print(result['formatted'][:2000])

if __name__ == "__main__":
    main()
