class Solution {
	private HashMap<Character, Integer> buildCharacterMap() {
		HashMap<Character, Integer> characterMap = new HashMap<>();

		for(char ch='a';ch<='z';ch++) {
			characterMap.put(ch, 0);
		}

		return characterMap;
	}
    public boolean isAnagram(String s, String t) {
		HashMap<Character, Integer> characterCount = buildCharacterMap();

		for(int i=0;i<s.length();i++) {
			characterCount.put(s.charAt(i), characterCount.get(s.charAt(i))+1);
		}

		for(int j=0;j<t.length();j++) {
			characterCount.put(t.charAt(j), characterCount.get(t.charAt(j))-1);
		}

		for(Integer value:characterCount.values()) {
			if(value<0 || value>0)return false;
		}

		return true;
    }
}
