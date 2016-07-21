package helloword;

import org.w3c.dom.css.ElementCSSInlineStyle;

public class TestVoidMethod {

	public static void main(String[] args) {
		printGrade(99);

	}

	public static void printGrade(double score) {
		if (score > 90) {
			System.out.println("very good");
		} else if (score > 80) {
			System.out.println("good");
		} else if (score > 70) {
			System.out.println("well");

		} else {
			System.out.println("bad");
		}

	}

}
