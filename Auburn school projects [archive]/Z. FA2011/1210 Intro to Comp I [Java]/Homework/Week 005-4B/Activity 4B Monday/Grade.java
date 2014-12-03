/**
*
*
*@author Albert Wallace - section 003
*
*@version 9/19/2011
*/
public class Grade {

	//instance variables
	private double exam1, exam2, finalExam;
	private double activityAvg;
	private double quizAvg;
	private double projectAvg;
	private String studentName;
	
	/**
	*More instance variables. These are constants to be used later.
	*/
	public static final int EXAM_1 = 0, EXAM_2 = 1, FINAL = 3;
	private static final double EXAM_WEIGHT = 0.15, FINAL_WEIGHT = 0.3,
		QUIZ_WEIGHT = 0.1, ACT_WEIGHT = 0.1,
		PROJ_WEIGHT = 0.2;
		
	/**
	*Constructor sets up the grade profile for a given student.
	*
	*@param nameIn accepts the name of the student for whom the grades
	* are being entered
	*/
	public Grade(String nameIn) {
		
		studentName = nameIn;
		
		}
	
		/**
		*
		*
		*@param activityAvgIn average score of activities, to be weighted
		*
		*@param quizAverageIn average score of quizzes, to be weighted
		*/	
	public void	setLabAverages(double activityAvgIn, double quizAverageIn) {
		
		activityAvg = activityAvgIn;
		quizAvg = quizAverageIn;
		
		}
	
		/**
		*
		*
		*@param examType sets the type of exam scored
		*
		*@param examScore sets the score of the exam
		*/	
	public void setExamScore(int examType, double examScore) {
		
		if (examType == EXAM_1) {
			exam1 = examScore;
			}
		else if (examType == EXAM_2) {
			exam2 = examScore;
			}
		else if (examType == FINAL) {
			finalExam = examScore;
			}
		
		}
		
		/**
		*
		*
		*@param average accepts average of project grades
		*/
	public void setProjectAverage(double average) {
		
		projectAvg = average;
		
		}
		
		/**
		*
		*
		*@return returns grade in class as a double
		*/
	public double calculateGrade() {
		
		double grade = (exam1 * EXAM_WEIGHT) + (exam2 * EXAM_WEIGHT)
			+ (finalExam * FINAL_WEIGHT) + (activityAvg * ACT_WEIGHT)
			+ (quizAvg * QUIZ_WEIGHT) + (projectAvg * PROJ_WEIGHT); //HW WEIGHT?
		
		return grade;
		}
		
		/**
		*Ultimately passes the student's name and final grade to
		* whatever may require it.
		*
		*@return returns properly formatted string
		*/
	public String toString() {
		
		
		return "Name: " + studentName + "\r\n" + "Final Grade: "
			+ calculateGrade();
		}

	
}