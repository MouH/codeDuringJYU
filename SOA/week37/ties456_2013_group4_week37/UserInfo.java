package ties456_2013_group4_week37;

public class UserInfo {
	String email, firstName, lastName, displayName;
	String gender, birthDate, location, website;
	String premium, bandwidth, created;
	boolean isValidated;
	
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getFirstName() {
		return firstName;
	}
	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}
	public String getLastName() {
		return lastName;
	}
	public void setLastName(String lastName) {
		this.lastName = lastName;
	}
	public String getDisplayName() {
		return displayName;
	}
	public void setDisplayName(String displayName) {
		this.displayName = displayName;
	}
	public String getGender() {
		return gender;
	}
	public void setGender(String gender) {
		this.gender = gender;
	}
	public String getBirthDate() {
		return birthDate;
	}
	public void setBirthDate(String birthDate) {
		this.birthDate = birthDate;
	}
	public String getLocation() {
		return location;
	}
	public void setLocation(String location) {
		this.location = location;
	}
	public String getWebsite() {
		return website;
	}
	public void setWebsite(String website) {
		this.website = website;
	}
	public String getPremium() {
		return premium;
	}
	public void setPremium(String premium) {
		this.premium = premium;
	}
	public String getBandwidth() {
		return bandwidth;
	}
	public void setBandwidth(String bandwidth) {
		this.bandwidth = bandwidth;
	}
	public String getCreated() {
		return created;
	}
	public void setCreated(String created) {
		this.created = created;
	}
	public boolean isValidated() {
		return isValidated;
	}
	public void setValidated(boolean isValidated) {
		this.isValidated = isValidated;
	}
	public UserInfo() {}
	@Override
	public String toString() {
		return "UserInfo [email=" + email + ", firstName=" + firstName
				+ ", lastName=" + lastName + ", displayName=" + displayName
				+ ", gender=" + gender + ", birthDate=" + birthDate
				+ ", location=" + location + ", website=" + website
				+ ", premium=" + premium + ", bandwidth=" + bandwidth
				+ ", created=" + created + ", isValidated=" + isValidated + "]";
	}
	
	
}
