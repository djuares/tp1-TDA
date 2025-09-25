import unittest

from problema4.problema_4 import subsequence_max_dynamic_programming

class TestSubsequenceMaxDynamicProgramming(unittest.TestCase):

    def test_empty_array(self):
        """Prueba con un array vacío: debe devolver suma 0 y subarray vacío."""
        # Arrange
        array = []
        expected_max_sum = 0
        expected_subarray_result = []

        # Act
        max_sum, start, end = subsequence_max_dynamic_programming(array)
        subarray_result = array[start:end + 1]

        # Assert
        self.assertEqual(max_sum, expected_max_sum)
        self.assertEqual(subarray_result, expected_subarray_result)

    def test_single_element(self):
        """Prueba con un array de un solo elemento: debe seleccionar ese elemento."""
        # Arrange
        array = [5]
        expected_max_sum = 5
        expected_subarray_result = [5]

        # Act
        max_sum, start, end = subsequence_max_dynamic_programming(array)
        subarray_result = array[start:end + 1]

        # Assert
        self.assertEqual(max_sum, expected_max_sum)
        self.assertEqual(subarray_result, expected_subarray_result)

    def test_all_negative(self):
        """Prueba con un array de todos negativos: debe seleccionar el mayor (menos negativo)."""
        # Arrange
        array = [-3, -1, -2]
        expected_max_sum = -1
        expected_subarray_result = [-1]

        # Act
        max_sum, start, end = subsequence_max_dynamic_programming(array)
        subarray_result = array[start:end + 1]

        # Assert
        self.assertEqual(max_sum, expected_max_sum)
        self.assertEqual(subarray_result, expected_subarray_result)

    def test_positive_max_sum(self):
        """Prueba con un array que tiene una subsecuencia con suma máxima positiva."""
        # Arrange
        array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected_max_sum = 6
        expected_subarray_result = [4, -1, 2, 1]

        # Act
        max_sum, start, end = subsequence_max_dynamic_programming(array)
        subarray_result = array[start:end + 1]

        # Assert
        self.assertEqual(max_sum, expected_max_sum)
        self.assertEqual(subarray_result, expected_subarray_result)

    def test_mixed_with_negatives(self):
        """Prueba con un array mixto donde la suma máxima incluye negativos."""
        # Arrange
        array = [-2, 1, 3, -1, 5]
        expected_max_sum = 8
        expected_subarray_result = [1, 3, -1, 5]

        # Act
        max_sum, start, end = subsequence_max_dynamic_programming(array)
        subarray_result = array[start:end + 1]

        # Assert
        self.assertEqual(max_sum, expected_max_sum)
        self.assertEqual(subarray_result, expected_subarray_result)

    def test_all_zeros(self):
        """Prueba con un array de todos ceros: debe seleccionar un solo cero."""
        # Arrange
        array = [0, 0, 0]
        expected_max_sum = 0
        expected_subarray_result = [0]

        # Act
        max_sum, start, end = subsequence_max_dynamic_programming(array)
        subarray_result = array[start:end + 1]

        # Assert
        self.assertEqual(max_sum, expected_max_sum)
        self.assertEqual(subarray_result, expected_subarray_result)

    def test_long_positive_sequence(self):
        """Prueba con una secuencia larga positiva: debe extender to_do el array."""
        # Arrange
        array = [1, 2, 3, 4, 5]
        expected_max_sum = 15
        expected_subarray_result = [1, 2, 3, 4, 5]

        # Act
        max_sum, start, end = subsequence_max_dynamic_programming(array)
        subarray_result = array[start:end + 1]

        # Assert
        self.assertEqual(max_sum, expected_max_sum)
        self.assertEqual(subarray_result, expected_subarray_result)

class TestSetDeDatosInforme(unittest.TestCase):

    def test_case_general(self):
        """Prueba con un caso general mixto de positivos, negativos y ceros."""
        # Arrange
        array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected_max_sum = 6
        expected_subarray_result = [4, -1, 2, 1]

        # Act
        max_sum, start, end = subsequence_max_dynamic_programming(array)
        subarray_result = array[start:end + 1]

        # Assert
        self.assertEqual(max_sum, expected_max_sum)
        self.assertEqual(subarray_result, expected_subarray_result)

    def test_all_positives(self):
        """Prueba con un array de todos positivos: debe seleccionar toda la secuencia."""
        # Arrange
        array = [1, 2, 3, 4]
        expected_max_sum = 10
        expected_subarray_result = [1, 2, 3, 4]

        # Act
        max_sum, start, end = subsequence_max_dynamic_programming(array)
        subarray_result = array[start:end + 1]

        # Assert
        self.assertEqual(max_sum, expected_max_sum)
        self.assertEqual(subarray_result, expected_subarray_result)

    def test_all_negatives(self):
        """Prueba con un array de todos negativos: debe seleccionar el mayor (menos negativo)."""
        # Arrange
        array = [-5, -1, -3]
        expected_max_sum = -1
        expected_subarray_result = [-1]

        # Act
        max_sum, start, end = subsequence_max_dynamic_programming(array)
        subarray_result = array[start:end + 1]

        # Assert
        self.assertEqual(max_sum, expected_max_sum)
        self.assertEqual(subarray_result, expected_subarray_result)

    def test_sandwich_case(self):
        """Prueba con un caso 'sándwich' donde la suma máxima está en el medio."""
        # Arrange
        array = [-10, 4, 2, -5, 8, -20]
        expected_max_sum = 9
        expected_subarray_result = [4, 2, -5, 8]

        # Act
        max_sum, start, end = subsequence_max_dynamic_programming(array)
        subarray_result = array[start:end + 1]

        # Assert
        self.assertEqual(max_sum, expected_max_sum)
        self.assertEqual(subarray_result, expected_subarray_result)