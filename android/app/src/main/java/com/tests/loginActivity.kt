package com.tests

import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class loginActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_login)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        val password: TextView = findViewById(R.id.LoginPassword)
        val email: TextView = findViewById(R.id.loginEmail)
        val login: Button = findViewById(R.id.loginButton)

        login.setOnClickListener {
            val mainInt = Intent(this, MainActivity::class.java)
            val isTrue = RegisterActivity.users.any{
                user -> user.userEmail == email.text.toString() &&
                user.password == password.text.toString()
            }

            if (isTrue){
                startActivity(mainInt)
            }
        }
    }
}