package com.tests

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class RegisterActivity : AppCompatActivity() {
    companion object{
        val users = mutableListOf<User>()
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_register)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        val registerButton: Button = findViewById(R.id.register_button)
        val email: EditText = findViewById(R.id.email_field)
        val password: EditText = findViewById(R.id.password_field)

        registerButton.setOnClickListener {
            val user = User(email.text.toString(), password.text.toString())
            users.add(user)

            val loginInt = Intent(this, loginActivity::class.java).apply {

            }
            startActivity(loginInt)
        }
    }
}